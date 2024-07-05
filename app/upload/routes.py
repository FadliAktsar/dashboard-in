from flask import render_template, request, redirect, flash, url_for,jsonify

from app.extension import db
from app.upload import bp
from app.models.transaksi import Transaksi

from io import StringIO
import pandas as pd
import csv

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
#@login_required
def index():
    
    try:
        #get transaction data from db and make it pagination
        page = request.args.get('page', 1, type=int)
        paginate = db.paginate(db.select(Transaksi)\
                               .order_by(Transaksi.Settlement_Date.desc()),
              page=page,
                per_page=10,
                  error_out=False)
        
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

    return render_template('upload/index.html', 
                           transaksi=paginate,
                           items=paginate.items,
                           pagination=paginate)

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
        csv_input = pd.read_csv(stream, delimiter=';', header=None)

        required_columns = [
            'Outlet_Name', 'Merchant_Id', 'Feature', 'Order_Id', 'Transaction_Id', 'Amount', 'Net_Amount',
            'Transaction_Status', 'Transaction_Time', 'Payment_Type', 'Payment_Date', 'GoPay_Transaction_Id',
            'GoPay_Reference_Id', 'GoPay_Customer_Id', 'Qris_Transaction_Type', 'Qris_Reference_Id', 'Qris_Issuer',
            'Qris_Acquirer', 'Card_Type', 'Credit_Card_Number', 'Settlement_Date', 'Settlement_Time'
        ]

        missing_columns = [col for col in required_columns if col not in csv_input.columns]
        if missing_columns:
            return jsonify({"message": f"Missing required columns: {', '.join(missing_columns)}", "success": False})

        # Use transaction to ensure atomicity
        with db.session.begin():
            for _, row in csv_input.iterrows():
                upload = Transaksi(
                    Outlet_Name=row['Outlet_Name'],
                    Merchant_Id=row['Merchant_Id'],
                    Feature=row['Feature'],
                    Order_Id=row['Order_Id'],
                    Transaction_Id=row['Transaction_Id'],
                    Amount=row['Amount'],
                    Net_Amount=row['Net_Amount'],
                    Transaction_Status=row['Transaction_Status'],
                    Transaction_Time=row['Transaction_Time'],
                    Payment_Type=row['Payment_Type'],
                    Payment_Date=row['Payment_Date'],
                    GoPay_Transaction_Id=row['GoPay_Transaction_Id'],
                    GoPay_Reference_Id=row['GoPay_Reference_Id'],
                    GoPay_Customer_Id=row['GoPay_Customer_Id'],
                    Qris_Transaction_Type=row['Qris_Transaction_Type'],
                    Qris_Reference_Id=row['Qris_Reference_Id'],
                    Qris_Issuer=row['Qris_Issuer'],
                    Qris_Acquirer=row['Qris_Acquirer'],
                    Card_Type=row['Card_Type'],
                    Credit_Card_Number=row['Credit_Card_Number'],
                    Settlement_Date=row['Settlement_Date'],
                    Settlement_Time=row['Settlement_Time']
                )
                db.session.add(upload)

        return jsonify({"message": "File successfully uploaded and data saved to database", "success": True})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error processing file: {e}", "success": False})