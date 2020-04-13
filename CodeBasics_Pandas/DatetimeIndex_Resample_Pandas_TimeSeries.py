# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:48:31 2020

@author: Rajesh
"""
DatetimeIndex and Resample :- 
----------------------------
import pandas as pd

df = pd.read_csv(r'E:\CodeBasics_Pandas\Pandas_CSV_CB\aapl.csv')
df.head()
-------------
       Date    Open    High     Low   Close    Volume
0  1-Jun-17  153.17  153.33  152.22  153.18  16404088
1  2-Jun-17  153.58  155.45  152.89  155.45  27770715
2  5-Jun-17  154.34  154.45  153.46  153.93  25331662
3  6-Jun-17  153.90  155.81  153.78  154.45  26624926
4  7-Jun-17  155.02  155.98  154.48  155.37  21069647

# We just want to know the Type of Date Column into dataset.
print(type('Date')) # <class 'str'>

# Here Date type is the string so we just have to convert it into Time and Date Format.
# We have one parameter like paras_date=[''].
df1 = pd.read_csv(r'E:\CodeBasics_Pandas\Pandas_CSV_CB\aapl.csv',parse_dates=['Date'],index_col='Date')
print(type(df['Date'][0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'> # Now it is converted into Timestamp format.

# Here we have chabged the default index = 'Date' now.
df1.index # It shows the Index values .

# If we want to retrive the JAN 2017 Stock Prices Values.

df1['2017'].head(2)
-------------
              Open    High     Low   Close    Volume
Date                                                
2017-06-01  153.17  153.33  152.22  153.18  16404088
2017-06-02  153.58  155.45  152.89  155.45  27770715

df1['2017'].Close.head(2)
------
Date
2017-06-01    153.18
2017-06-02    155.45
Name: Close, dtype: float64

# To find the average of the Jan 2017 Price.
df1['2017'].Close.mean() # 147.83136363636365

df1['2017-06-07':'2017-06-01']# It shows the result for that Particular date.

# It will be giving the result.

df1.Close.resample('M').mean()
# Date
2017-06-30    147.831364
Freq: M, Name: Close, dtype: float64

%matplotlib inline
df1.Close.resample('M').mean().plot() # Monthly.

df1.Close.resample('W').mean().plot() # Weekly

df1.Close.resample('Q').mean().plot() # Quarterly

df1.Close.resample('B').mean().plot() # Bussiness Daywise


df1.Close.plot() # It shows the details as per daily daywise.




