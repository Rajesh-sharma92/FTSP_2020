# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:25:31 2020

@author: Rajesh
"""

Period and PeriodIndex Pandas Time Series :- 
-------------------------------------------

import pandas as pd

# How to create the Year Period.
y = pd.Period('2020')

y # Period('2020', 'A-DEC')

dir(y) # It contains so many Attributes & parameters to use it.

y.start_time # Timestamp('2020-01-01 00:00:00')

y.end_time # Timestamp('2020-12-31 23:59:59.999999999')

# How to create the Month Period.
m = pd.Period('2020-4',freq='M')
m # Period('2020-04', 'M')

m.start_time # Timestamp('2020-04-01 00:00:00')

m.end_time # Timestamp('2020-04-30 23:59:59.999999999')

# If we want to perform some of the operations like Adding one more month to Date.

m = pd.Period('2020-4',freq='M')
m+1 # Period('2020-05', 'M')

m = pd.Period('2020-12',freq='M')
m+2 # Period('2021-02', 'M')

# Now we will be creating the day time .
d = pd.Period('2020-02-27')
d # Period('2020-02-27', 'D') # By default it takes the "D" Frequency. If we want we can pass it as Explicitly.

d = pd.Period('2020-02-27',freq='D')
d+2 #  Period('2020-02-29', 'D')

d = pd.Period('2020-02-29',freq='D')
d+1 #  Period('2020-03-01', 'D')

# How to check the leap year or not.
# We will be adding 1 day extra to 28th feb to any year.
d = pd.Period('2020-02-28',freq='D')
d+1 # Period('2020-02-29', 'D') --> It's leap year coz it is same month only.

d = pd.Period('2021-02-28',freq='D')
d+1 # Period('2021-03-01', 'D') --> It's not leap year coz it is not same month it's changed.

# Now we will be creating the Hourly based frequency.
h = pd.Period('2021-02-28 23:00:00',freq='H')
h # Period('2021-02-28 23:00', 'H')

h.start_time # Timestamp('2021-02-28 23:00:00')

h.end_time # Timestamp('2021-02-28 23:59:59.999999999')

h+1 # Period('2021-03-01 00:00', 'H')

NOTE :- The above task we can also do it by using Pandas Library.

h + pd.offsets.Hour(1) # Period('2021-03-01 00:00', 'H')

h + pd.offsets.Hour(25) # Period('2021-03-02 00:00', 'H')

# We do the substraction also.
h - 10 # Period('2021-02-28 13:00', 'H')

h + pd.offsets.Hour(2) # Period('2021-03-01 01:00', 'H')

# To check it by Quarter also.
q = pd.Period('2020Q1')
q # Period('2020Q1', 'Q-DEC')

q + 1 # Period('2020Q2', 'Q-DEC')

q.start_time # Timestamp('2020-01-01 00:00:00')

q.end_time # Timestamp('2020-03-31 23:59:59.999999999')

NOTE :- In the Walmart there will be fical year Means New Year will be starting from feb 1st onwards and ending at 1st Jan.

# Here we just need to change the frequecy of the " freq='Jan'".
q = pd.Period('2020Q1' , freq='Q-JAN')
q # Period('2020Q1', 'Q-JAN')

q.start_time # Timestamp('2019-02-01 00:00:00')

q.end_time # Timestamp('2019-04-30 23:59:59.999999999')


# Here we just want to convert Quartely frequency into monthly frequency.
q.asfreq('M' , how='start') # Period('2019-02', 'M')

q.start_time # Timestamp('2019-02-01 00:00:00')

q.end_time # Timestamp('2019-04-30 23:59:59.999999999')


q = pd.Period('2020Q1' , freq='Q-JAN') # Period('2020Q1', 'Q-JAN')

q2 = pd.Period('2021Q2' , freq='Q-JAN') # Period('2021Q2', 'Q-JAN')

q2 - q # <5 * QuarterEnds: startingMonth=1>


# Now let's create the Period Index.
idx = pd.period_range('2019','2020',freq='Q')
idx
-----
PeriodIndex(['2019Q1', '2019Q2', '2019Q3', '2019Q4', '2020Q1'], 
            dtype='period[Q-DEC]', freq='Q-DEC')

# Now let's create the Period Index for Walmart Company.
idx = pd.period_range('2019','2020',freq='Q-JAN')
idx
----------
PeriodIndex(['2019Q4', '2020Q1', '2020Q2', '2020Q3', '2020Q4'], 
            dtype='period[Q-JAN]', freq='Q-JAN')

idx[0].start_time # Timestamp('2018-11-01 00:00:00')

idx[0].end_time # Timestamp('2019-01-31 23:59:59.999999999')

# If we want to geneerate the 10 periods.
idx = pd.period_range('2020', periods=10, freq='Q-JAN')
idx
-----
PeriodIndex(['2020Q4', '2021Q1', '2021Q2', '2021Q3', '2021Q4', '2022Q1',
             '2022Q2', '2022Q3', '2022Q4', '2023Q1'],
            dtype='period[Q-JAN]', freq='Q-JAN')



# Here we can use the Numpy model to create the series.
import numpy as np
ps = pd.Series(np.random.randn(len(idx)),idx)
ps
---------
2020Q4    1.703067
2021Q1   -1.633204
2021Q2    1.093589
2021Q3    1.440037
2021Q4    0.214262
2022Q1    1.528263
2022Q2   -0.842827
2022Q3    0.733723
2022Q4    1.161957
2023Q1   -1.020464
Freq: Q-JAN, dtype: float64

# How to get the period index here.
ps.index
----
PeriodIndex(['2020Q4', '2021Q1', '2021Q2', '2021Q3', '2021Q4', '2022Q1',
             '2022Q2', '2022Q3', '2022Q4', '2023Q1'],
            dtype='period[Q-JAN]', freq='Q-JAN')


ps['2020':'2021']
--------
020Q4    1.703067
2021Q1   -1.633204
2021Q2    1.093589
2021Q3    1.440037
2021Q4    0.214262
2022Q1    1.528263
2022Q2   -0.842827
2022Q3    0.733723
2022Q4    1.161957
Freq: Q-JAN, dtype: float64


# How to convert into the date & time Index.
pst = ps.to_timestamp()
pst
-----------------
2019-11-01    1.703067
2020-02-01   -1.633204
2020-05-01    1.093589
2020-08-01    1.440037
2020-11-01    0.214262
2021-02-01    1.528263
2021-05-01   -0.842827
2021-08-01    0.733723
2021-11-01    1.161957
2022-02-01   -1.020464
Freq: QS-NOV, dtype: float64

pst.index
-----------
DatetimeIndex(['2019-11-01', '2020-02-01', '2020-05-01', '2020-08-01',
               '2020-11-01', '2021-02-01', '2021-05-01', '2021-08-01',
               '2021-11-01', '2022-02-01'],
              dtype='datetime64[ns]', freq='QS-NOV')

# To convert back into period index.
pst.to_period() 
-------
2019Q4    1.703067
2020Q1   -1.633204
2020Q2    1.093589
2020Q3    1.440037
2020Q4    0.214262
2021Q1    1.528263
2021Q2   -0.842827
2021Q3    0.733723
2021Q4    1.161957
2022Q1   -1.020464
Freq: Q-DEC, dtype: float64

-------------------------------------------------------------------------------------

# Now here we will one of the exerice on to the Walmart dataset.

import pandas as pd

df = pd.read_csv('E:\CodeBasics_Pandas\Pandas_CSV_CB\wmt.csv')
df
-----
 Line Item  2017Q1  2017Q2  2017Q3  2017Q4  2018Q1
0   Revenue  115904  120854  118179  130936  117542
1  Expenses   86544   89485   87484   97743   87688
2    Profit   29360   31369   30695   33193   29854

df.set_index('Line Item',inplace=True)
df
---
           2017Q1  2017Q2  2017Q3  2017Q4  2018Q1
Line Item                                        
Revenue    115904  120854  118179  130936  117542
Expenses    86544   89485   87484   97743   87688
Profit      29360   31369   30695   33193   29854

# Now we will us the " T property like row--> cols and cols--> row ".
df = df.T
df
---
Line Item  Revenue  Expenses  Profit
2017Q1      115904     86544   29360
2017Q2      120854     89485   31369
2017Q3      118179     87484   30695
2017Q4      130936     97743   33193
2018Q1      117542     87688   29854

df.index
# Index(['2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1'], dtype='object')

df.index = pd.PeriodIndex(df.index,freq='Q-JAN')
df.index
-------
PeriodIndex(['2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1'], 
            dtype='period[Q-JAN]', freq='Q-JAN')


df['start date'] = df.index.map(lambda x : x.start_time)
df
---------
Line Item  Revenue  Expenses  Profit start date
2017Q1      115904     86544   29360 2016-02-01
2017Q2      120854     89485   31369 2016-05-01
2017Q3      118179     87484   30695 2016-08-01
2017Q4      130936     97743   33193 2016-11-01
2018Q1      117542     87688   29854 2017-02-01

df['end date'] = df.index.map(lambda x : x.end_time)
df
----
Line Item  Revenue  Expenses  Profit start date                      end date
2017Q1      115904     86544   29360 2016-02-01 2016-04-30 23:59:59.999999999
2017Q2      120854     89485   31369 2016-05-01 2016-07-31 23:59:59.999999999
2017Q3      118179     87484   30695 2016-08-01 2016-10-31 23:59:59.999999999
2017Q4      130936     97743   33193 2016-11-01 2017-01-31 23:59:59.999999999
2018Q1      117542     87688   29854 2017-02-01 2017-04-30 23:59:59.999999999


