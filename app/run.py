import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app.extension import db
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima

df = pd.read_sql_query(db)
