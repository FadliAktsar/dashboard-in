from flask import render_template, jsonify, request
from app.extension import db
from app.dashboard import bp
from sqlalchemy import func
from app.models.transaksi import Transaksi
import datetime
import joblib
import pandas as pd

model = joblib.load('app/notebooks/model.joblib')

@bp.route('/')
#@login_required
def index():
    return render_template('dashboard/index.html')

def daterange(start_date, end_date):
    for n in range(int((end_date-start_date).days)+1):
        yield  start_date + datetime.timedelta(n)

@bp.route('/get_data')
def get_data():
    try:    
        #Earliest and Latest Transaction Dates
        earliest_date = db.session.query(func.min(Transaksi.Settlement_Date)).scalar()
        latest_date = db.session.query(func.max(Transaksi.Settlement_Date)).scalar()

        if earliest_date is None or latest_date is None:
            return jsonify({'data':[], 'labels':[]})

        #DB Query
        transaction = db.session.execute(
            db.select(Transaksi.Settlement_Date,
                      func.sum(Transaksi.Amount).label("Revenue")).group_by(Transaksi.Settlement_Date).order_by(Transaksi.Settlement_Date)
        ).all()
    
        # Convert Query Result to a Dictionary
        transaction_dict = {t[0]: t[1] for t in transaction}

        # Convert to list of dictionaries
        labels = []
        data = []

        for single_date in daterange(earliest_date, latest_date):
            labels.append(single_date.strftime('%Y-%m-%d'))
            if single_date in transaction_dict:
                data.append(transaction_dict[single_date])
            else:
                data.append(0)
        
        # Handle forecast input
        input_periods = int(request.args.get('periods', 30))  # Default forecast period is 30 days
        forecast_range = pd.date_range(start=latest_date + datetime.timedelta(days=1),
                                        periods=input_periods, freq='D')
        
        # Forecast using ARIMA model
        transaction_series = pd.Series(data, index=pd.to_datetime(labels))
        prediction = model.get_prediction(start=len(transaction_series), end=len(transaction_series) + input_periods - 1)
        prediction_mean = prediction.predicted_mean

        # Prepare forecast labels and data
        forecast_labels = [date.strftime('%Y-%m-%d') for date in forecast_range]
        forecast_data = prediction_mean.tolist()

        return jsonify({
            'data': data,
              'labels': labels,
                'forecast_labels': forecast_labels,
                    'forecast_data': forecast_data
                  })
    
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text