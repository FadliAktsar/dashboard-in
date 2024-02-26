from flask import render_template, request, flash
#from flask_login import login_required, current_user
import pickle
from abc import ABC, abstractclassmethod

from app.peramalan import bp
with open('app/arima_model.pkl', 'rb') as file:
    model = pickle.load(file)

@bp.route('/', methods=['GET', 'POST'])
#@login_required
def index():

    if request.method == 'POST':
        try:     
            # Ambil data input dari formulir
            input_data = request.form.get('input_data')
            # Lakukan peramalan menggunakan model
            hasil_ramalan = model.predict([input_data])
        except ValueError:
            flash('Error.')
        # Render template atau tampilkan hasil peramalan
        return render_template('hasil_ramalan.html', hasil_ramalan=hasil_ramalan)
 
    return render_template('peramalan/index.html')
