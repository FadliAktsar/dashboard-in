from flask import render_template, request, jsonify, current_app

from app.extension import db
from app.upload import bp
from app.models.transaksi import Transaksi
from sqlalchemy import or_,func, cast, String

from io import StringIO
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
def index():
    return render_template('upload/index.html')

@bp.route('/api', methods=['GET'])
def data():
     
     query = Transaksi.query
     
     #Search Filter
     search = request.args.get('search[value]')
     if search:
          query = query.filter(db.or_(
                Transaksi.Transaction_Id.ilike(f'%{search}%'),
                cast(Transaksi.Amount, String).ilike(f'%{search}%'),
                func.to_char(
                    Transaksi.Settlement_Date, 'YYYY-MM-DD'
                    ).ilike(f'%{search}%'),
                func.to_char(
                 Transaksi.Payment_Date, 'YYYY-MM-DD'  
                ).ilike(f'%{search}%'),
                Transaksi.Payment_Type.ilike(f'%{search}%')
               ))
          total_filtered = query.count()

     # Sorting
     order = []
     i = 0
     while True:
               col_index = request.args.get(f'order[{i}][column]')
               if col_index is None:
                    break
               col_name = request.args.get(f'columns[{col_index}][data]')
               if col_name not in ['Settlement_Date', 'Payment_Type']:
                    col_name = 'Settlement_Date'
               descending = request.args.get(f'order[{i}][dir]') == 'desc'
               col = getattr(Transaksi, col_name)
               if descending:
                    col = col.desc()
               order.append(col)
               i += 1
     if order:
         query = query.order_by(*order)

     # Paggination
     start = request.args.get('start', type=int)
     length = request.args.get('length', type=int)
     total_filtered = query.count()
     query = query.offset(start).limit(length)
    
     def clean_data(transaksi_dict):
        for key, value in transaksi_dict.items():
            if value != value:  # Memeriksa jika nilai adalah NaN
                transaksi_dict[key] = None
            elif isinstance(value, float) and abs(value) > 1e10:  # Memeriksa angka dengan notasi E
                transaksi_dict[key] = '{:.0f}'.format(value)
        return transaksi_dict
     
     response = {
         'data': [clean_data(transaksi.to_dict()) for transaksi in query.all()],
         'recordsFiltered': total_filtered,
         'recordsTotal': Transaksi.query.count(),
         'draw': request.args.get('draw', type=int)
         }
          
     return jsonify(response)

@bp.route('/upload_files', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        return jsonify({"message": "No file part", "success": False})

    csv_file = request.files['file']

    if csv_file.filename == '':
        return jsonify({"message": "No selected file", "success": False})

    if not allowed_file(csv_file.filename):
        return jsonify({"message": "File type not allowed", "success": False})

    try:
        stream = StringIO(csv_file.stream.read().decode("UTF8"), newline=None)
        csv_input = pd.read_csv(stream, delimiter=';', header=0)

        required_columns = [
            'Outlet name', 'Merchant ID', 'Feature', 'Order ID', 'Transaction ID', 'Amount', 'Net Amount',
            'Transaction Status', 'Transaction time', 'Payment Type', 'Payment Date', 'GO-PAY Transactions ID',
            'Gopay Reference Id', 'GoPay Customer ID', 'QRIS Transaction Type', 'QRIS Reference ID', 'QRIS Issuer',
            'QRIS Acquirer', 'Card Type', 'Credit Card Number', 'Settlement Date', 'Settlement time'
        ]

        missing_columns = [col for col in required_columns if col not in csv_input.columns]
        if missing_columns:
            return jsonify({"message": f"Missing required columns: {', '.join(missing_columns)}",
                             "success": False})
        
        # Use transaction to ensure atomicity
        with db.session.no_autoflush:
            for _, row in csv_input.iterrows():

                existing_transaction = Transaksi.query.filter_by(Transaction_Id=row['Transaction ID']).first()

                if existing_transaction:
                     current_app.logger.info("Transaction already exists with ID: %s", row['Transaction ID'])
                     return jsonify({"message": "Data already exist", "success": False})
                
                def parese_date(date_str):
                    
                    if len(date_str) == 8:
                        try:
                            return datetime.strptime(date_str, '%Y%m%d').date()
                        except ValueError:
                            return datetime.strptime(date_str, '%d%m%Y').date()
                    
                    if len(date_str) == 10:
                        try:
                            return datetime.strptime(date_str, '%Y/%m/%d').date()
                        except ValueError:
                            return datetime.strptime(date_str, '%d/%m/%Y').date()
                        
                    raise ValueError(f"Date format for {date_str} is not supported")

                new_transaction = Transaksi(
                    Outlet_Name=row['Outlet name'],
                    Merchant_Id=row['Merchant ID'],
                    Feature=row['Feature'],
                    Order_Id=row['Order ID'],
                    Transaction_Id=row['Transaction ID'],
                    Amount=row['Amount'],
                    Net_Amount=row['Net Amount'],
                    Transaction_Status=row['Transaction Status'],
                    Transaction_Time=row['Transaction time'],
                    Payment_Type=row['Payment Type'],
                    Payment_Date= parese_date(row['Payment Date']),
                    GoPay_Transaction_Id=row['GO-PAY Transactions ID'],
                    GoPay_Reference_Id=row['Gopay Reference Id'],
                    GoPay_Customer_Id=row['GoPay Customer ID'],
                    Qris_Transaction_Type=row['QRIS Transaction Type'],
                    Qris_Reference_Id=row['QRIS Reference ID'],
                    Qris_Issuer=row['QRIS Issuer'],
                    Qris_Acquirer=row['QRIS Acquirer'],
                    Card_Type=row['Card Type'],
                    Credit_Card_Number=row['Credit Card Number'],
                    Settlement_Date=parese_date(row['Settlement Date']),
                    Settlement_Time=row['Settlement time']
                )

                db.session.add(new_transaction)

            db.session.commit()  # Commit Data After Looping Process
        return jsonify({"message": "File successfully uploaded and data saved to database", "success": True})
    
    except Exception as e:
        db.session.rollback()
        logging.error("Error processing file: %s", e, exc_info=True)
        return jsonify({"message": f"Error processing file: {e}", "success": False})