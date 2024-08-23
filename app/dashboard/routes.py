from flask import render_template, jsonify, request, make_response
from app.extension import db
from app.dashboard import bp
from sqlalchemy import func

from app.models.transaksi import Transaksi
from app.models.peramalan import Peramalan

import logging
import datetime
import joblib
import pandas as pd
import csv
from io import StringIO

model = joblib.load('app/notebooks/arima_model_weekly_third.joblib')

@bp.route('/')
def index():
    return render_template('dashboard/index.html')

def daterange(start_date, end_date):
    for n in range(int((end_date-start_date).days)+1):
        yield  start_date + datetime.timedelta(n)

@bp.route('/get_data')
def get_data():
    try:   
        # Parameter untuk mengatur mode tampilan (daily atau weekly)
        mode = request.args.get('mode', 'daily')  # Default 'daily'
        
        #Earliest and Latest Transaction Dates
        earliest_date = db.session.query(func.min(Transaksi.Settlement_Date)).scalar()
        latest_date = db.session.query(func.max(Transaksi.Settlement_Date)).scalar()

        if earliest_date is None or latest_date is None:
            return jsonify({'data':[], 'labels':[], 'forecast_labels':[], 'forecast_data':[]})

        labels = []
        data = []

         # DB Query berdasarkan mode (daily atau weekly)
        if mode == 'weekly':
             transaction = db.session.execute(
                db.select(func.date_trunc('week', Transaksi.Settlement_Date).cast(db.Date).label('week_start'),
                          func.sum(Transaksi.Amount).label("Revenue"))\
                            .group_by('week_start')\
                                .order_by('week_start')
            ).all()
             
             #print("Weekly transactions:", transaction)  # Debug output
             
             transaction_dict = {t[0]: t[1] for t in transaction}
             print("Keys in transaction_dict:")
             for key in transaction_dict.keys():
                 print(key, type(key))
                 
             # Looping berdasarkan minggu dari revenue per hari
             for single_date in pd.date_range(start=earliest_date, end=latest_date, freq='W-MON'):
                date_str = single_date.date()
                print(f"Checking date: {date_str} in transaction_dict")  # Debugging
                labels.append(date_str.strftime('%Y-%m-%d'))  # Label dimulai dari data mingguan
                
                if date_str in transaction_dict:
                    data.append(transaction_dict[date_str])
                else:
                    print(f"{date_str} not found, appending 0")
                    data.append(0)          

        else: #Mode default
            transaction = db.session.execute(
                db.select(Transaksi.Settlement_Date,
                        func.sum(Transaksi.Amount).label("Revenue"))\
                            .group_by(Transaksi.Settlement_Date)\
                                .order_by(Transaksi.Settlement_Date)
            ).all()

            # Convert Query Result to a Dictionary
            transaction_dict = {t[0]: t[1] for t in transaction}

            for single_date in daterange(earliest_date, latest_date):
                labels.append(single_date.strftime('%Y-%m-%d'))
    
                if single_date in transaction_dict:
                    data.append(transaction_dict[single_date])
                else:
                    data.append(0)
        
        
        # Handle forecast input
        periods = request.args.get('periods', '4')
        try:
            input_periods = int(periods)
        except ValueError:
            input_periods = 4

        forecast_range = pd.date_range(start=latest_date + datetime.timedelta(days=1),
                                        periods=input_periods, freq='W')
        
        # Forecast using ARIMA model
        transaction_series = pd.Series(data,
                                        index=pd.to_datetime(labels))
        prediction = model.predict(start=len(transaction_series),
                                           end=len(transaction_series) + input_periods - 1)

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
        logging.error(f"Error in /get_data route: {error_text}")
        return jsonify({'error': error_text})

@bp.route('/download_csv')
def download_csv():
    try:

        forecasts = db.session.query(Peramalan).order_by(Peramalan.Settlement_Date ).all()

        # Create a CSV file in memory
        si = StringIO()
        cw = csv.writer(si)
        cw.writerow(['Settlement_Date', 'Forecast'])
        for pred in forecasts:
            cw.writerow([pred.Settlement_Date, pred.Forecast])
        
        # Return the CSV file as a response
        response = make_response(si.getvalue())
        response.headers['Content-Disposition'] = 'attachment; filename=predictions.csv'
        response.headers['Content-type'] = 'text/csv'
        return response
    
    except Exception as e:
        error_text = "The error:" + str(e)
        logging.error(f"Error in /get_data route: {error_text}")
        return jsonify({'error': error_text})