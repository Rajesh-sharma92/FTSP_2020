# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:42:58 2020

@author: Rajesh
"""

to_datetime Pandas TimeSeries :-
------------------------------
Here We can see that 5th JAN 2017 may be written like this.

1) '2017-01-05'

2) 'Jan 5, 2017'

3) '01/05/2017'

4) '2017.01.05'

5) '2017/01/05'

import pandas as pd

dates = ['2017-01-05','Jan 5, 2017','01/05/2017','2017.01.05','2017/01/05']

# Here we pass the all date formats and It will be working properly.
pd.to_datetime(dates)
------------
['2017-01-05', '2017-01-05', '2017-01-05', '2017-01-05',
               '2017-01-05'],

# Here we can pass the Date as well as Time also.
dates = ['2017-01-05 2:30:00 PM','Jan 5, 2017 14:30:00','01/05/2017 10:15:00 AM','2017.01.05','2017/01/05']

pd.to_datetime(dates)
----------
['2017-01-05 14:30:00', '2017-01-05 14:30:00',
               '2017-01-05 10:15:00', '2017-01-05 00:00:00',
               '2017-01-05 00:00:00'],


NOTE :-  In the USA Date Format is the :- mm/dd/yyyy

In the Europe Data Format is the :- dd/mm/yyyy
 
pd.to_datetime('5/1/2017')
# Timestamp('2017-05-01 00:00:00')
pd.to_datetime('5/1/2017', dayfirst=True)
# Timestamp('2017-01-05 00:00:00')

# For the example if we have the Date In the Below format then how to handle it.
# Here delimeter is '$' to sepearted in the place of '/'.
pd.to_datetime('5 $ 1 $ 2017') # ValueError: ('Unknown string format:', '5 $ 1 $ 2017')

If we delcared the format also then it will be working.
pd.to_datetime('5 $ 1 $ 2017' , format='%d $ %m $ %Y')
#  Timestamp('2017-01-05 00:00:00')

pd.to_datetime('5 # 1 # 2017' , format='%d # %m # %Y')
# Timestamp('2017-01-05 00:00:00')

# If we have dates in this format then it will throw an error to avoid such error 
# we need to delcared those errors as ' errors = ignore '.
dates = ['2017-01-05 2:30:00 PM','Jan 5, 2017 14:30:00','01/05/2017 10:15:00 AM','2017.01.05','abc']

pd.to_datetime(dates) # ValueError: ('Unknown string format:', 'abc')

pd.to_datetime(dates , errors='ignore') 
------------
['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00',
       '01/05/2017 10:15:00 AM', '2017.01.05', 'abc']

NOTE :- It will just ignore that kind of above errors and It will not be conveted into DateTime Format.

# If we want to convert the rest of the string into DateTime Format then 
# We need to declared ' errors = coerce '.
     
pd.to_datetime(dates , errors='coerce') 
-------------
['2017-01-05 14:30:00', '2017-01-05 14:30:00',
               '2017-01-05 10:15:00', '2017-01-05 00:00:00',
                               'NaT']

NOTE :- If we have the Time for such kind of then what to do.
Epoch(Unix Time) is the number of seconds that have passed since Jan 1,1970 00:00:00 UTC.

t = 1586873128
pd.to_datetime(t)
# Timestamp('1970-01-01 00:00:01.586873128')
 
t1 = 1586959747 
pd.to_datetime(t1)
# Timestamp('1970-01-01 00:00:01.586959747')

t = 1586873128
dt = pd.to_datetime([t] , unit='s')
# Timestamp('2020-04-14 14:05:28')
print(dt)
# DatetimeIndex(['2020-04-14 14:05:28'], dtype='datetime64[ns]', freq=None)

# Again comeback to original format Epoch.
dt.view('int64')
# array([1586873128000000000], dtype=int64)

