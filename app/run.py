import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima

from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:Duapuluhenam0299@localhost:5432/database_in')

df = pd.read_sql('SELECT * FROM public.transaksi', engine)
relevant_columns = (df['Net_Amount'] !=0)