from flask import render_template, redirect, url_for, request
#from flask_login import login_required, current_user
from app.extension import db
from app.model.transaksi import Transaksi
from app.upload import bp

@bp.route('/', methods=['GET', 'POST'])
#@login_required
def index():
    
    '''
    Settlement_Date =
    Amount =
    Payment_Type =
    '''
    #get transaction data from db
    transaksi = db.session.execute(
            db.select(Transaksi).filter_by(Settlement_Date=Transaksi.Settlement_Date, Amount=Transaksi.Amount, Payment_Type=Transaksi.Payment_Type)
        )
    
    for trans in transaksi:
       pass

    if request.method == 'POST':
        pass

    return render_template('upload/index.html')
