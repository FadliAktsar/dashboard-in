import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima

from extension import app,db

with app.app_context():
    # Mendapatkan koneksi ke database
    conn = db.engine.connect()

    # Query SQL
    sql = """
        SELECT "Settlement_Date", "Amount", "Net_Amount" FROM public.transaksi;
    """

    # Membaca data dari database ke DataFrame pandas
    df = pd.read_sql(sql, conn)

    # Menampilkan lima baris pertama dari DataFrame
    print(df.head())