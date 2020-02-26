# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:49:57 2020

@author: Rajesh
"""

Handle Missing Data: fillna , dropna & interpolate :- 
--------------------------------------------------
1) fillna :- To fill the missing value using different ways.
2) Interpolate :- To make a guess on missing values using interpolation.
3) dropna :- To drop rows with missing values.

import pandas as pd

df = pd.read_csv(r'E:\Forsk Pandas\NYC_Wheather_data.csv')
print(df)

************ Result ***********
        day  Temperature  windspeed   event
0   3/1/2020         32.0        6.0    Rain
1   3/4/2020          NaN        9.0   Sunny
2   3/5/2020         28.0        NaN    Snow
3   3/8/2020          NaN        7.0     NaN
4  3/10/2020         32.0        NaN    Rain
5  3/15/2020          NaN        NaN   Sunny
6  3/18/2020          NaN        NaN     NaN
7  3/23/2020         34.0        8.0  Cloudy
8  3/26/2020         40.0       12.0   Sunny

-----------------------------------------------------------------------------------------------------
print(type('day')) # str
print(type(df['day'][0])) # str

Question :- How to change the day(string data) into number data.
Answer :- We just need to use the concept "parse_dates=['day']".

import pandas as pd

df = pd.read_csv(r'E:\Forsk Pandas\NYC_Wheather_data.csv' , parse_dates = ['day'])
print(type(df['day'][0])) # <class 'pandas._libs.tslibs.timestamps.Timestamp'>

print(df)

************ Result ***********

         day  Temperature  windspeed   event
0 2020-03-01         32.0        6.0    Rain
1 2020-03-04          NaN        9.0   Sunny
2 2020-03-05         28.0        NaN    Snow
3 2020-03-08          NaN        7.0     NaN
4 2020-03-10         32.0        NaN    Rain
5 2020-03-15          NaN        NaN   Sunny
6 2020-03-18          NaN        NaN     NaN
7 2020-03-23         34.0        8.0  Cloudy
8 2020-03-26         40.0       12.0   Sunny

---------------------------------------------------------------------------------------------------
df.set_index('day', inplace = True)
print(df)

            Temperature  windspeed   event
day                                       
2020-03-01         32.0        6.0    Rain
2020-03-04          NaN        9.0   Sunny
2020-03-05         28.0        NaN    Snow
2020-03-08          NaN        7.0     NaN
2020-03-10         32.0        NaN    Rain
2020-03-15          NaN        NaN   Sunny
2020-03-18          NaN        NaN     NaN
2020-03-23         34.0        8.0  Cloudy
2020-03-26         40.0       12.0   Sunny

--------------------------------------------------------------------------------------------------------
Question :- How to fill all the missing values of NaN ? 
Answer :- By using fillna(n) # where n is number.

new_df = df.fillna(0)
print(new_df)

        Temperature  windspeed   event
day                                       
2020-03-01         32.0        6.0    Rain
2020-03-04          0.0        9.0   Sunny
2020-03-05         28.0        0.0    Snow
2020-03-08          0.0        7.0       0
2020-03-10         32.0        0.0    Rain
2020-03-15          0.0        0.0   Sunny
2020-03-18          0.0        0.0       0
2020-03-23         34.0        8.0  Cloudy
2020-03-26         40.0       12.0   Sunny
NaT                 0.0        0.0       0
----------------------------------------------------------------------------------------
Question :- Can we fill the missing values by different values not like same value all data into different cols ?
Answer :- Yes, Offcourse. We can do it easily and we just need to pass value into python dictionary form like "cols Name : values".

new_df = df.fillna({
        'Temperature' : 0 ,
        'windspeed' : 0 ,
        'event' : 'No event'
        })
print(new_df)

           Temperature  windspeed     event
day                                         
2020-03-01         32.0        6.0      Rain
2020-03-04          0.0        9.0     Sunny
2020-03-05         28.0        0.0      Snow
2020-03-08          0.0        7.0  No event
2020-03-10         32.0        0.0      Rain
2020-03-15          0.0        0.0     Sunny
2020-03-18          0.0        0.0  No event
2020-03-23         34.0        8.0    Cloudy
2020-03-26         40.0       12.0     Sunny
NaT                 0.0        0.0  No event
-----------------------------------------------------------------------------------------------------
Question :- How to fill the missing values like 32.0 was temp on that date & 0.0 was on this is date.
So, It is not the correct temp. What we can do to avoid this temp ?
Answer :- We just need to use one method that is " method = 'ffill' ".

new_df = df.fillna(method = 'ffill') # ffill means forward fill values.
print(new_df)

           Temperature  windspeed   event
day                                       
2020-03-01         32.0        6.0    Rain
2020-03-04         32.0        9.0   Sunny
2020-03-05         28.0        9.0    Snow
2020-03-08         28.0        7.0    Snow
2020-03-10         32.0        7.0    Rain
2020-03-15         32.0        7.0   Sunny
2020-03-18         32.0        7.0   Sunny
2020-03-23         34.0        8.0  Cloudy
2020-03-26         40.0       12.0   Sunny
NaT                40.0       12.0   Sunny
-----------------------------------------------------------------------------------------------------
new_df = df.fillna(method = 'bfill') # bfill means backward fill values.
print(new_df)

           Temperature  windspeed   event
day                                       
2020-03-01         32.0        6.0    Rain
2020-03-04         28.0        9.0   Sunny
2020-03-05         28.0        7.0    Snow
2020-03-08         32.0        7.0    Rain
2020-03-10         32.0        8.0    Rain
2020-03-15         34.0        8.0   Sunny
2020-03-18         34.0        8.0  Cloudy
2020-03-23         34.0        8.0  Cloudy
2020-03-26         40.0       12.0   Sunny
NaT                 NaN        NaN     NaN
-----------------------------------------------------------------------------------------------------------
Question :- How to copy the missing data into dataFrame like Horizental or row wise ?
Answer :- Yes. we can by using bfillna & columns.

new_df = df.fillna(method='bfill' , axis = 'columns')
print(new_df)

          Temperature windspeed   event
day                                     
2020-03-01          32         6    Rain
2020-03-04           9         9   Sunny
2020-03-05          28      Snow    Snow
2020-03-08           7         7     NaN
2020-03-10          32      Rain    Rain
2020-03-15       Sunny     Sunny   Sunny
2020-03-18         NaN       NaN     NaN
2020-03-23          34         8  Cloudy
2020-03-26          40        12   Sunny
NaT                NaN       NaN     NaN
----------------------------------------------------------------------------------------
Question :- How to fill the value into missing dataframes but and If we are filling by using the carry Farward method.
but we just want to fill for 1 cell only.
Answer :- Yes, We can fill the value for 1 cell also by using to set the limit on the filling values. like = " limit = 1 "

df = pd.read_csv(r'E:\Forsk Pandas\NYC_Wheather_data.csv')
print(df)

new_df = df.fillna(method='ffill' , limit = 1)
print(new_df)

        day  Temperature  windspeed   event
0   3/1/2020         32.0        6.0    Rain
1   3/4/2020         32.0        9.0   Sunny
2   3/5/2020         28.0        9.0    Snow
3   3/8/2020         28.0        7.0    Snow
4  3/10/2020         32.0        7.0    Rain
5  3/15/2020         32.0        NaN   Sunny
6  3/18/2020          NaN        NaN   Sunny
7  3/23/2020         34.0        8.0  Cloudy
8  3/26/2020         40.0       12.0   Sunny
9  3/26/2020         40.0       12.0   Sunny
------------------------------------------------------------------------------------------------
Question :- How to use the interpolate method into dataframes ?
Answer :- We can use " interpolate() " method into dataframes while reading the csv file and it always shows the middle of that 2 nos.

new_df = df.interpolate()
print(new_df)

NOTE :- We can see that in the temparature there is 32 & 28 and middle no. between two nos. is 30.but it is not near by 28. we will doing like thi 
new_df = df.interpolate(method = 'time')
print(new_df)
-----------------------------------------------------------------------------------------------------
Question :- How to drop the NaN values present into all cols ?
Answer :- Yes. We can drop all the NaN values from DataFrames by using the method of dropna().

new_df = df.dropna() # It drops all the values which are NaN into DataFrames.
print(new_df)

       day  Temperature  windspeed   event
0   3/1/2020         32.0        6.0    Rain
7  3/23/2020         34.0        8.0  Cloudy
8  3/26/2020         40.0       12.0   Sunny
------------------------------------------------------------------------------------------------
Question :- How to check all the NaN values present into dataFrames ?
Answer :- Yes. we Can check by using the " how = 'all' " paramaters.

new_df = df.dropna(how='all') # It shows all NaN values.
print(new_df)

     day  Temperature  windspeed   event
0   3/1/2020         32.0        6.0    Rain
1   3/4/2020          NaN        9.0   Sunny
2   3/5/2020         28.0        NaN    Snow
3   3/8/2020          NaN        7.0     NaN
4  3/10/2020         32.0        NaN    Rain
5  3/15/2020          NaN        NaN   Sunny
6  3/18/2020          NaN        NaN     NaN
7  3/23/2020         34.0        8.0  Cloudy
8  3/26/2020         40.0       12.0   Sunny
----------------------------------------------------------------------------------------------------
new_df = df.dropna(thresh = 2)
print(new_df)
-------------------------------------------------------------------------------------
Question :- How to insert the missing date into dataframes file ?
Answer :- By using the data_range('','') method.

dt = pd.date_range('03-02-2020' , '03-03-2020')
idx = pd.DatetimeIndex(dt)
df= df.reindex(idx)
print(df)
-----------------------------------------------------------------------------------------------------



































































































































































































































































