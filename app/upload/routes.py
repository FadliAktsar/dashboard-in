from flask import render_template, request, jsonify

from app.extension import db
from app.upload import bp
from app.models.transaksi import Transaksi
from sqlalchemy import or_,func, cast, String

from io import StringIO
import pandas as pd

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
def index():
    
    try:
        #get transaction data from db and make it pagination
        search_query = request.args.get('search', '', type=str)
        page = request.args.get('page', 1, type=int)

        query = db.session.query(Transaksi).order_by(Transaksi.Settlement_Date.desc())

        if search_query:
            search_filter = or_(
                Transaksi.Transaction_Id.ilike(f'%{search_query}%'),
                cast(Transaksi.Amount, String).ilike(f'%{search_query}%'),
                func.to_char(
                    Transaksi.Settlement_Date, 'YYYY-MM-DD'
                    ).ilike(f'%{search_query}%'),
                func.to_char(
                 Transaksi.Payment_Date, 'YYYY-MM-DD'  
                ).ilike(f'%{search_query}%'),
                Transaksi.Payment_Type.ilike(f'%{search_query}%')
            )
            query = query.filter(search_filter)
        
        paginate = db.paginate(query, page=page, per_page=10, error_out=False)
        
    except Exception as e:
        error_text = "The error:" + str(e)
        hed = 'Something is broken.'
        return hed + "/" + error_text
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({
            "table": render_template('upload/_transaction_table.html', transaksi=paginate.items),
            "pagination": render_template('upload/_pagination.html', pagination=paginate, search_query=search_query)
        })

    return render_template('upload/index.html', 
                           transaksi=paginate,
                           items=paginate.items,
                           pagination=paginate,
                           search_query=search_query)

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
        with db.session.begin():
            for _, row in csv_input.iterrows():

                existing_transaction = Transaksi.query.filter_by(Transaction_Id=row['Transaction ID']).first()

                if existing_transaction:
                     return jsonify({"message": "Data already exist", "success": False})
                
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
                    Payment_Date=row['Payment Date'],
                    GoPay_Transaction_Id=row['GO-PAY Transactions ID'],
                    GoPay_Reference_Id=row['Gopay Reference Id'],
                    GoPay_Customer_Id=row['GoPay Customer ID'],
                    Qris_Transaction_Type=row['QRIS Transaction Type'],
                    Qris_Reference_Id=row['QRIS Reference ID'],
                    Qris_Issuer=row['QRIS Issuer'],
                    Qris_Acquirer=row['QRIS Acquirer'],
                    Card_Type=row['Card Type'],
                    Credit_Card_Number=row['Credit Card Number'],
                    Settlement_Date=row['Settlement Date'],
                    Settlement_Time=row['Settlement time']
                )

                db.session.add(new_transaction)

            db.session.commit()  # Komit setelah loop selesai
        return jsonify({"message": "File successfully uploaded and data saved to database", "success": True})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error processing file: {e}", "success": False})