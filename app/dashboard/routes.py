from flask import render_template, jsonify, request, make_response
from app.extension import db
from app.dashboard import bp
from sqlalchemy import func

from app.models.transaksi import Transaksi
from app.models.peramalan import Peramalan

import datetime
import joblib
import pandas as pd
import csv
from io import StringIO

model = joblib.load('app/notebooks/arima_model1.joblib')

@bp.route('/')
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
                      func.sum(Transaksi.Amount).label("Revenue"))\
                        .group_by(Transaksi.Settlement_Date)\
                            .order_by(Transaksi.Settlement_Date)
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
        transaction_series = pd.Series(data,
                                        index=pd.to_datetime(labels))
        prediction = model.predict(start=len(transaction_series),
                                           end=len(transaction_series) + input_periods - 1)

        #Save Forecast to Database
        for i, date in enumerate(forecast_range):
            existing_entry = db.session.query(Peramalan).filter_by(Settelement_Date=date).first()
            if not existing_entry:
                predict = Peramalan(Settelement_Date=date, Forecast = prediction[i],Revenue=0)
                db.session.add(predict)
        db.session.commit()

        # Prepare forecast labels and data
        forecast_labels = [date.strftime('%Y-%m-%d') for date in forecast_range]
        forecast_data = prediction.tolist()

        return jsonify({
            'data': data,
              'labels': labels,
                'forecast_labels': forecast_labels,
                    'forecast_data': forecast_data
                  })
    
    except Exception as e:
        error_text = "The error:" + str(e)
        hed = 'Something is broken.'
        return hed + "/" + error_text

@bp.route('/download_csv')
def download_csv():
    try:

        forecasts = db.session.query(Peramalan).order_by(Peramalan.Settelement_Date).all()

        # Create a CSV file in memory
        si = StringIO()
        cw = csv.writer(si)
        cw.writerow(['Settlement_Date', 'Forecast'])
        for pred in forecasts:
            cw.writerow([pred.Settelement_Date, pred.Forecast])
        
        # Return the CSV file as a response
        response = make_response(si.getvalue())
        response.headers['Content-Disposition'] = 'attachment; filename=predictions.csv'
        response.headers['Content-type'] = 'text/csv'
        return response
    
    except Exception as e:

        error_text = "The error:" + str(e)
        hed = 'Something is broken.'
        return hed + "/" + error_text