from flask import render_template, request, flash, jsonify
from app.extension import db
from app.dashboard import bp
from sqlalchemy import func
from app.models.transaksi import Transaksi

@bp.route('/')
#@login_required
def index():

    return render_template('dashboard/index.html')

@bp.route('/get_data')
def get_data():
    try:    
    
        transaction = db.session.execute(
            db.select(Transaksi.Settlement_Date,
                      func.sum(Transaksi.Amount).label("Revenue")).group_by(Transaksi.Settlement_Date).order_by(Transaksi.Settlement_Date)
        ).all()

        # Convert to list of dictionaries
        labels = [t[0].strftime('%Y-%m-%d') for t in transaction]
        data = [t[1] for t in transaction]

        return jsonify({'data': data, 'labels': labels})
    
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@bp.route('/forecast')
def forecast():
    pass