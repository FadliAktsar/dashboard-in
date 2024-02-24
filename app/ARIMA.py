#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import os
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#Main Laptop
file_path = 'C:/Users/HELLO/OneDrive/Desktop/skripsi/dataset-in'


# In[ ]:


#Dania Laptop
#file_path = 'C:/Users/Dania/OneDrive/Desktop/DESKTOP/Mas Aktsar/Skripsi/File Skripsi_V1_1_1/dataset_kopiin'


# # Connect to Database

# ### Connect with iPython

# In[3]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[9]:


get_ipython().run_line_magic('env', 'DATABASE_URL=postgresql://postgres:Duapuluhenam0299@localhost:5432/database_in')


# ### Connect with sqlalchemy

# In[4]:


from sqlalchemy import create_engine


# In[5]:


engine = create_engine('postgresql://postgres:Duapuluhenam0299@localhost:5432/database_in')


# ### Writing SQL with connection

# In[19]:


get_ipython().run_line_magic('sql', 'SELECT * FROM public.transaksi')


# ### Access Database and Store to Dataframe

# In[6]:


database_df = pd.read_sql('SELECT * FROM public.transaksi', engine)


# In[7]:


database_df


# # Data Preparation

# ## Read CSV / Datasets

# ### Before Reverse

# In[4]:


'''
df_agustus = pd.read_csv(file_path+'/raw_before_reverse/1_dataset_transaksi_agustus.csv',delimiter=';')
df_september = pd.read_csv(file_path+'/raw_before_reverse/2_dataset_transaksi_september.csv',delimiter=';')
df_oktober = pd.read_csv(file_path+'/raw_before_reverse/3_dataset_transaksi_oktober.csv',delimiter=';')
df_november = pd.read_csv(file_path+'/raw_before_reverse/4_dataset_transaksi_november.csv',delimiter=';')
'''


# ### After Reverse

# In[5]:


#Read CSV After Reverse
'''
import glob
file_names = glob.glob(file_path+'/raw_after_reverse/*.csv')
'''


# --------------------------------------------------

# ## Reverse Datasets

# In[6]:


'''
dfAgustusReversed = df_agustus[::-1].reset_index(drop=True)
dfSeptemberReversed = df_september[::-1].reset_index(drop=True)
dfOktoberReversed = df_oktober[::-1].reset_index(drop=True)
dfNovemberReversed = df_november[::-1].reset_index(drop=True)
'''


# In[7]:


'''
dfAgustusReversed.to_csv('C:/Users/Dania/OneDrive/Desktop/DESKTOP/Mas Aktsar/Skripsi/File Skripsi_V1/dataset_kopiin/raw_after_reverse/1_dataset_transaksi_agustus_reversed.csv')
dfSeptemberReversed.to_csv('C:/Users/Dania/OneDrive/Desktop/DESKTOP/Mas Aktsar/Skripsi/File Skripsi_V1/dataset_kopiin/raw_after_reverse/2_dataset_transaksi_september_reversed.csv')
dfOktoberReversed.to_csv('C:/Users/Dania/OneDrive/Desktop/DESKTOP/Mas Aktsar/Skripsi/File Skripsi_V1/dataset_kopiin/raw_after_reverse/3_dataset_transaksi_oktober_reversed.csv')
dfNovemberReversed.to_csv('C:/Users/Dania/OneDrive/Desktop/DESKTOP/Mas Aktsar/Skripsi/File Skripsi_V1/dataset_kopiin/raw_after_reverse/4_dataset_transaksi_november_reversed.csv')
'''


# ## Combine Datasets

# In[8]:


'''
li = []
'''


# In[9]:


'''
for filename in file_names:
    df = pd.read_csv(filename, index_col=None, header=0, delimiter=';')
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)
'''


# In[10]:


'''
frame.to_csv('C:/Users/Dania/OneDrive/Desktop/DESKTOP/Mas Aktsar/Skripsi/File Skripsi_V1/dataset_kopiin/raw_data_transaksi_kopiin.csv')
'''


# # Data Preprocessing

# ## Resample Data and Index

# In[4]:


df = pd.read_csv(file_path+'/raw_data_transaksi_kopiin.csv', index_col=None, header=0, delimiter=';')


# In[13]:


#Select Some Columns For Needs

df1 = df[['Outlet name','Merchant ID', 'Feature', 
    #'Order ID', 
    'Transaction ID',
       'Amount', 'Net Amount', 'Transaction Status', 
        #'Transaction time',
       'Payment Type', 
        #'Payment Date', 
       'GO-PAY Transactions ID',
       'Gopay Reference Id', 
       #'GoPay Customer ID', 
       'QRIS Transaction Type',
       'QRIS Reference ID', 'QRIS Issuer', 'QRIS Acquirer', 
       #'Card Type',
       #'Credit Card Number',
       'Settlement Date', 
    #'Settlement time'
        ]].copy()


# In[14]:


df1.dtypes


# In[9]:


relevant_columns = (database_df['Net_Amount'] !=0)


# In[11]:


#Subset Net Amount to Amount
database_df.loc[relevant_columns, 'Amount'] = database_df.loc[relevant_columns, 'Net_Amount']


# In[12]:


database_df['Amount']


# ### For Forecasting DataFrame

# In[18]:


database_df.columns


# In[22]:


df2 = database_df[[
    #'Outlet_Name', 'Merchant_Id', 'Feature', 'Order_Id', 'Transaction_Id',
       'Amount',
    #'Net_Amount', 'Transaction_Status', 'Transaction_Time',
       #'Payment_Type', 'Payment_Date', 'GoPay_Transaction_Id',
       #'GoPay_Reference_Id', 'GoPay_Customer_Id', 'Qris_Transaction_Type',
       #'Qris_Reference_Id', 'Qris_Issuer', 'Qris_Acquirer', 'Card_Type',
       #'Credit_Card_Number', 
    'Settlement_Date',
    #'Settlement_Time'
]].copy()


# In[23]:


df2['Settlement_Date'] = pd.to_datetime(df2['Settlement_Date'])
df2.set_index('Settlement_Date', inplace=True)


# In[24]:


df2


# In[26]:


df2 = df2.groupby(['Settlement_Date'])['Amount'].sum().reset_index().copy()


# In[27]:


#Rename Column
df2 = df2.rename(columns={
    'Amount':'Amount_Per_Day'
})


# In[28]:


df2['Settlement_Date'] = pd.to_datetime(df2['Settlement_Date'], format='%d/%m/%Y')
df2.set_index('Settlement_Date', inplace=True)
df2.sort_index(inplace=True)


# In[29]:


plt.figure(figsize=(15, 10))
plt.plot(df2['Amount_Per_Day'], scalex=1)
plt.ylabel('Amount')
plt.title('Transaction over Time')
plt.show()


# # Data Modeling With ARIMA

# In[42]:


from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima


# ## Train & Test Datasets

# In[43]:


# Train & Test Datasets 1
train_df = df2.iloc[:51]
test_df = df2.iloc[51:]


# In[44]:


print(train_df.shape, test_df.shape)


# In[45]:


# Train & Test Datasets 2
train_df2 = df2.iloc[:56]
test_df2 = df2.iloc[56:]


# In[46]:


print(train_df2.shape, test_df2.shape)


# In[47]:


# Train & Test Datasets 3
train_df3 = df2.iloc[:60]
test_df3 = df2.iloc[60:]


# In[48]:


print(train_df3.shape, test_df3.shape)


# In[49]:


df2.index


# ------------------------------------------------------------

# ## Stationarity Test

# In[37]:


'''
plt.figure(figsize=(15, 10))
plt.plot(train_df['Amount_Per_Day'], scalex=1)
plt.plot(test_df['Amount_Per_Day'], scalex=1)
plt.ylabel('Amount')
plt.title('Transaction over Time - Train & Test Data 1')
plt.show()
'''


# In[50]:


def stationarity_test(value):
    df2['Amount_Per_Day'] = df2.sum(axis=1)
    result = adfuller(value, autolag='AIC')
    print('Uji Stasionaritas:')
    print('ADF Statistic:', result[0])
    print('P-Value', result[1])
    print('Number of Lags:', result[2])
    print('Number of Observation Used in the Analysis:', result[3])
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'\t{key}: {value}')
    if result[1] <= 0.05:
        print('Data Amount_Per_Day SUDAH STASIONER')
    else:
        print('Data Amount_Per_Day BELUM STASIONER')


# In[51]:


stationarity_test(df2)


# In[52]:


stationarity_test(train_df)


# In[53]:


stationarity_test(train_df2)


# In[54]:


stationarity_test(train_df3)


# ### Stationarity Test Valued:
# 
# notes: Stationer if P-Value < 0.05
# 
# - train_df (51 rows : 60%) = P-Value 0.029066843634943097
# - train_df2 (56 rows : 65%) = P-Value 3.56187722318105e-06
# - train_df3 (60 rows : 70%) = P-Value 5.008804986822835e-07525311813663e-10

# ## Hyperparameter Tuning

# ### auto_arima

# In[55]:


# Fit auto_arima to the training data to find the best parameters
model = auto_arima(train_df3['Amount_Per_Day'], start_p = 1, max_p = 6, 
    start_q = 1, max_q = 6, d=0, suppress_warning=True,
    seasonal = False, trace = True, stepwise=False)
#train_df3 = train_df3.asfreq('D')  # tetapkan frekuensi harian (sesuaikan sesuai kebutuhan)
# Print the best parameters
print(model.order)  # This will give you the values for (p, d, q)
#print('The best (p, d, q) model from auto_arima based on the data is:', model.order)


# In[56]:


p, d, q = 1, 0, 4
model_fitting= ARIMA(train_df3['Amount_Per_Day'], order=(p,d,q))
arima_result = model_fitting.fit()


# In[57]:


arima_result.summary()


# In[58]:


import pickle


# In[59]:


with open('arima_model.pkl', 'wb') as f:
    pickle.dump(arima_result, f)


# -----------------------------------------------------------

# ### manual method using ACF and PACF grafic

# In[ ]:


def manual_model(dataset):
    #ACF & PACF plots

    lag_acf = acf(dataset, nlags=12)
    lag_pacf = pacf(dataset, nlags=12, method='ols')
    
    # Plot ACF and PACF
    plt.figure(figsize=(12, 6))
    
    #Plot ACF
    plt.subplot(121)
    plt.stem(range(len(lag_acf)), lag_acf)
    #plt.plot(lag_acf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96/np.sqrt(len(dataset)), linestyle='--', color='gray')
    plt.axhline(y=1.96/np.sqrt(len(dataset)), linestyle='--', color='gray')
    plt.title('Autocorrelation Function')
    
    #Plot PACF
    plt.subplot(122)
    plt.stem(range(len(lag_pacf)), lag_pacf)
    #plt.plot(lag_pacf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96/np.sqrt(len(dataset)), linestyle='--', color='gray')
    plt.axhline(y=1.96/np.sqrt(len(dataset)), linestyle='--', color='gray')
    plt.title('Partial Autocorrelation Function')
    
    plt.tight_layout()
    plt.show()


# In[ ]:


manual_model(train_df3)


# ### Data Forecasting

# #### _solving problem_ 

# In[ ]:


start=len(train_df3)
end=len(train_df3)+len(test_df3)-1


# In[ ]:


forecast_results = arima_result.get_prediction(start=start, end=end, dynamic=False)
forecast_values = forecast_results.predicted_mean
conf_int = forecast_results.conf_int()
forecast_df = pd.DataFrame({'Forecast': forecast_values})


# In[ ]:


forecast_df.index = df2.index[start:end+1]


# In[ ]:


print(forecast_df)


# In[ ]:


merged_df = pd.concat([forecast_df, test_df3], axis=1)


# In[ ]:


merged_df = merged_df.reset_index().copy()


# In[ ]:


print(merged_df['Forecast'].describe())


# In[ ]:


merged_df['Amount_Per_Day'].describe()


# In[ ]:


merged_df


# In[ ]:


plt.figure(figsize=(10, 6))
plt.plot(train_df3.index, train_df3['Amount_Per_Day'], label='Train Data')
plt.plot(forecast_df.index, forecast_df['Forecast'], label='Forecast', color='red')
plt.plot(test_df3.index, test_df3['Amount_Per_Day'], label='Test Data', color='green')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Amount over Time with ARIMA Forecast')
plt.legend()
plt.show()


# ## Evaluasi Peramalan Data

# In[ ]:


rmse = mean_squared_error(merged_df['Amount_Per_Day'], merged_df['Forecast'], squared=False)
mae = mean_absolute_error(merged_df['Amount_Per_Day'], merged_df['Forecast'])
mape = mean_absolute_percentage_error(merged_df['Amount_Per_Day'], merged_df['Forecast'])

print('Root Mean Squared Error (RMSE):', rmse)
print('Mean Absolute Error (MAE):', mae)
print('Mean Absolute Percentage Error (MAPE):', mape)


# ---------------------------------------------------------
