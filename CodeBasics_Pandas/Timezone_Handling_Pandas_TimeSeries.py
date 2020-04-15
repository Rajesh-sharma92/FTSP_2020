# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:36:17 2020

@author: Rajesh
"""
Read microsoft's intraday stock prize :- 
---------------------------------------

import pandas as pd
df = pd.read_csv("E:\CodeBasics_Pandas\Pandas_CSV_CB\msft.csv", header=1,index_col='Date Time',parse_dates=True)
df
------
                    Price
Date Time                 
2017-08-17 09:00:00  72.38
2017-08-17 09:15:00  71.00
2017-08-17 09:30:00  71.67
2017-08-17 10:00:00  72.80
2017-08-17 10:30:00  73.00
2017-08-17 11:00:00  72.50

df.index
-----
DatetimeIndex(['2017-08-17 09:00:00', '2017-08-17 09:15:00',
               '2017-08-17 09:30:00', '2017-08-17 10:00:00',
               '2017-08-17 10:30:00', '2017-08-17 11:00:00'],
              dtype='datetime64[ns]', name='Date Time', freq=None)

"""
Two types of datetimes in python
Naive (no timezone awareness)
Timezone aware datetime
Convert naive DatetimeIndex to timezone aware DatetimeIndex using tz_localize
"""
df.tz_localize(tz='US/Eastern')
df
-----
                    Price
Date Time                 
2017-08-17 09:00:00  72.38
2017-08-17 09:15:00  71.00
2017-08-17 09:30:00  71.67
2017-08-17 10:00:00  72.80
2017-08-17 10:30:00  73.00
2017-08-17 11:00:00  72.50

df.index = df.index.tz_localize(tz='US/Eastern')
df.index
-----------
DatetimeIndex(['2017-08-17 09:00:00-04:00', '2017-08-17 09:15:00-04:00',
               '2017-08-17 09:30:00-04:00', '2017-08-17 10:00:00-04:00',
               '2017-08-17 10:30:00-04:00', '2017-08-17 11:00:00-04:00'],
              dtype='datetime64[ns, US/Eastern]', name='Date Time', freq=None)

'''
Convert to Berlin time using tz_convert :- 
'''
df = df.tz_convert('Europe/Berlin')
df
-----
                          Price
Date Time                       
2017-08-17 15:00:00+02:00  72.38
2017-08-17 15:15:00+02:00  71.00
2017-08-17 15:30:00+02:00  71.67
2017-08-17 16:00:00+02:00  72.80
2017-08-17 16:30:00+02:00  73.00
2017-08-17 17:00:00+02:00  72.50

df.index
----------
DatetimeIndex(['2017-08-17 15:00:00+02:00', '2017-08-17 15:15:00+02:00',
               '2017-08-17 15:30:00+02:00', '2017-08-17 16:00:00+02:00',
               '2017-08-17 16:30:00+02:00', '2017-08-17 17:00:00+02:00'],
              dtype='datetime64[ns, Europe/Berlin]', name='Date Time', freq=None)


# To get the Time zones from all the Centuries.
from pytz import all_timezones
print(all_timezones) # It will be showing the all time Zone here.

'''
Convert to Mumbai time :- 
'''

# tz database doesn't have any Mumbai timezone but 
# calcutta and mumbai are both in same timezone so we will use that
df.index = df.index.tz_convert('Asia/Calcutta') 
df
-----
Date Time                       
2017-08-17 18:30:00+05:30  72.38
2017-08-17 18:45:00+05:30  71.00
2017-08-17 19:00:00+05:30  71.67
2017-08-17 19:30:00+05:30  72.80
2017-08-17 20:00:00+05:30  73.00
2017-08-17 20:30:00+05:30  72.50

'''
Using timezones in date_range :- 
'''

(1) timezone using pytz :- 

london = pd.date_range('3/6/2012 00:09:00', periods=10, freq='H',tz='Europe/London')
london
-------
DatetimeIndex(['2012-03-06 00:09:00+00:00', '2012-03-06 01:09:00+00:00',
               '2012-03-06 02:09:00+00:00', '2012-03-06 03:09:00+00:00',
               '2012-03-06 04:09:00+00:00', '2012-03-06 05:09:00+00:00',
               '2012-03-06 06:09:00+00:00', '2012-03-06 07:09:00+00:00',
               '2012-03-06 08:09:00+00:00', '2012-03-06 09:09:00+00:00'],
              dtype='datetime64[ns, Europe/London]', freq='H')


(2) timezone using dateutil :- 

td = pd.date_range('3/6/2012 00:00', periods=10, freq='H',tz='dateutil/Europe/London')
td
----
DatetimeIndex(['2012-03-06 00:00:00+00:00', '2012-03-06 01:00:00+00:00',
               '2012-03-06 02:00:00+00:00', '2012-03-06 03:00:00+00:00',
               '2012-03-06 04:00:00+00:00', '2012-03-06 05:00:00+00:00',
               '2012-03-06 06:00:00+00:00', '2012-03-06 07:00:00+00:00',
               '2012-03-06 08:00:00+00:00', '2012-03-06 09:00:00+00:00'],
              dtype='datetime64[ns, tzfile('GB-Eire')]', freq='H')

'''
Pandas documentation indicates that difference between pytz timezone and dateutil timezones is
In pytz you can find a list of common (and less common) time zones using from pytz import common_timezones, all_timezones
dateutil uses the OS timezones so there isn’t a fixed list available. For common zones, the names are the same as pytz
Airthmetic between different timezones
'''

rng = pd.date_range(start="2017-08-22 09:00:00",periods=10, freq='30min')
s = pd.Series(range(10),index=rng)
s
----
2017-08-22 09:00:00    0
2017-08-22 09:30:00    1
2017-08-22 10:00:00    2
2017-08-22 10:30:00    3
2017-08-22 11:00:00    4
2017-08-22 11:30:00    5
2017-08-22 12:00:00    6
2017-08-22 12:30:00    7
2017-08-22 13:00:00    8
2017-08-22 13:30:00    9
Freq: 30T, dtype: int64


b = s.tz_localize(tz="Europe/Berlin")
b
----
2017-08-22 09:00:00+02:00    0
2017-08-22 09:30:00+02:00    1
2017-08-22 10:00:00+02:00    2
2017-08-22 10:30:00+02:00    3
2017-08-22 11:00:00+02:00    4
2017-08-22 11:30:00+02:00    5
2017-08-22 12:00:00+02:00    6
2017-08-22 12:30:00+02:00    7
2017-08-22 13:00:00+02:00    8
2017-08-22 13:30:00+02:00    9
Freq: 30T, dtype: int64


m = s.tz_localize(tz="Asia/Calcutta")
m.index
----------
DatetimeIndex(['2017-08-22 09:00:00+05:30', '2017-08-22 09:30:00+05:30',
               '2017-08-22 10:00:00+05:30', '2017-08-22 10:30:00+05:30',
               '2017-08-22 11:00:00+05:30', '2017-08-22 11:30:00+05:30',
               '2017-08-22 12:00:00+05:30', '2017-08-22 12:30:00+05:30',
               '2017-08-22 13:00:00+05:30', '2017-08-22 13:30:00+05:30'],
              dtype='datetime64[ns, Asia/Calcutta]', freq='30T')

print(m)
-----------
2017-08-22 09:00:00+05:30    0
2017-08-22 09:30:00+05:30    1
2017-08-22 10:00:00+05:30    2
2017-08-22 10:30:00+05:30    3
2017-08-22 11:00:00+05:30    4
2017-08-22 11:30:00+05:30    5
2017-08-22 12:00:00+05:30    6
2017-08-22 12:30:00+05:30    7
2017-08-22 13:00:00+05:30    8
2017-08-22 13:30:00+05:30    9
Freq: 30T, dtype: int64


# It will first convert individual timezones to UTC and then align datetimes to 
# perform addition/subtraction etc. operations
b + m
-------
2017-08-22 03:30:00+00:00     NaN
2017-08-22 04:00:00+00:00     NaN
2017-08-22 04:30:00+00:00     NaN
2017-08-22 05:00:00+00:00     NaN
2017-08-22 05:30:00+00:00     NaN
2017-08-22 06:00:00+00:00     NaN
2017-08-22 06:30:00+00:00     NaN
2017-08-22 07:00:00+00:00     7.0
2017-08-22 07:30:00+00:00     9.0
2017-08-22 08:00:00+00:00    11.0
2017-08-22 08:30:00+00:00     NaN
2017-08-22 09:00:00+00:00     NaN
2017-08-22 09:30:00+00:00     NaN
2017-08-22 10:00:00+00:00     NaN
2017-08-22 10:30:00+00:00     NaN
2017-08-22 11:00:00+00:00     NaN
2017-08-22 11:30:00+00:00     NaN
Freq: 30T, dtype: float64

