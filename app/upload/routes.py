from flask import render_template, redirect, url_for, request
#from flask_login import login_required, current_user
from app.extension import db
from app.models.transaksi import Transaksi
from app.upload import bp

@bp.route('/')
#@login_required
def index():
    
    try:
        #get transaction data from db and make it pagination
        page = request.args.get('page', 1, type=int)
        paginate = db.paginate(db.select(Transaksi).order_by(Transaksi.Settlement_Date.desc()),
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
                            