# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:40:48 2020

@author: Rajesh
"""
Holidays Pandas Time Series :- 
---------------------------

import pandas as pd

df = pd.read_csv(r'E:\CodeBasics_Pandas\Pandas_CSV_CB\aapl_no_dates.csv')
df.head()
-------------
     Open    High     Low   Close    Volume
0  153.17  153.33  152.22  153.18  16404088
1  153.58  155.45  152.89  155.45  27770715
2  154.34  154.45  153.46  153.93  25331662
3  153.90  155.81  153.78  154.45  26624926
4  155.02  155.98  154.48  155.37  21069647

# Here we will check the Holidays are not be included into dataset. B = 'Business daywise'
pd.date_range(start='7/1/2017',end='7/21/2017',freq='B')
-------------
DatetimeIndex(['2017-07-03', '2017-07-04', '2017-07-05', '2017-07-06',
               '2017-07-07', '2017-07-10', '2017-07-11', '2017-07-12',
               '2017-07-13', '2017-07-14', '2017-07-17', '2017-07-18',
               '2017-07-19', '2017-07-20', '2017-07-21'],
              dtype='datetime64[ns]', freq='B')

# Here '2017-07-04'in the USA Indepant day holiday and It should not included at all.
# So, we need to remove it all those holidays form the USA Calalender list.
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay 

usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())
print(usb) # <CustomBusinessDay>

# Now, Again we will be checking the holidays list as per USA Calander details.
pd.date_range(start='7/1/2017',end='7/21/2017',freq=usb)
------------
DatetimeIndex(['2017-07-03', '2017-07-05', '2017-07-06', '2017-07-07',
               '2017-07-10', '2017-07-11', '2017-07-12', '2017-07-13',
               '2017-07-14', '2017-07-17', '2017-07-18', '2017-07-19',
               '2017-07-20', '2017-07-21'],
              dtype='datetime64[ns]', freq='C')

# Note :- Here we can see that we don't have any kind of holidays into the USA details.

# The above details are correct as per requiremnt so we can change it now.
rng = pd.date_range(start='7/1/2017',end='8/2/2017',freq=usb)

df.set_index(rng,inplace=True)
df.head()
-------------
              Open    High     Low   Close    Volume
2017-07-03  153.17  153.33  152.22  153.18  16404088
2017-07-05  153.58  155.45  152.89  155.45  27770715
2017-07-06  154.34  154.45  153.46  153.93  25331662
2017-07-07  153.90  155.81  153.78  154.45  26624926
2017-07-10  155.02  155.98  154.48  155.37  21069647

# we can create our own calander like this below.
can define your own calendar using AbstractHolidayCalendar as shown below. 
USFederalHolidayCalendar is the only calendar available in pandas library and it 
serves as an example for those who want to write their own custom calendars. 
Here is the link for USFederalHolidayCalendar implementation 
https://github.com/pandas-dev/pandas/blob/master/pandas/tseries/holiday.py

AbstractHolidayCalendar :- 


from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
class myCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('My Birth Day', month=9, day=1),#, observance=nearest_workday),
    ]
    
my_bday = CustomBusinessDay(calendar=myCalendar())
pd.date_range('9/1/2017','9/30/2017',freq=my_bday)

# It shows the correct result as per requirements.
DatetimeIndex(['2017-09-04', '2017-09-05', '2017-09-06', '2017-09-07',
               '2017-09-08', '2017-09-11', '2017-09-12', '2017-09-13',
               '2017-09-14', '2017-09-15', '2017-09-18', '2017-09-19',
               '2017-09-20', '2017-09-21', '2017-09-22', '2017-09-25',
               '2017-09-26', '2017-09-27', '2017-09-28', '2017-09-29'],
              dtype='datetime64[ns]', freq='C')


CustomBusinessDay :- 
------------------
Weekend in egypt is Friday and Saturday. Sunday is just a normal weekday and you can 
handle this custom week schedule using CystomBysinessDay with weekmask as shown below.

egypt_weekdays = "Sun Mon Tue Wed Thu"

b = CustomBusinessDay(weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)
------------------
DatetimeIndex(['2017-07-02', '2017-07-03', '2017-07-04', '2017-07-05',
               '2017-07-06', '2017-07-09', '2017-07-10', '2017-07-11',
               '2017-07-12', '2017-07-13', '2017-07-16', '2017-07-17',
               '2017-07-18', '2017-07-19', '2017-07-20', '2017-07-23',
               '2017-07-24', '2017-07-25', '2017-07-26', '2017-07-27'],
              dtype='datetime64[ns]', freq='C')


NOTE :- You can also add holidays to this custom business day frequency.

b = CustomBusinessDay(holidays=['2017-07-04', '2017-07-10'], weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)
-------------
DatetimeIndex(['2017-07-02', '2017-07-03', '2017-07-05', '2017-07-06',
               '2017-07-09', '2017-07-11', '2017-07-12', '2017-07-13',
               '2017-07-16', '2017-07-17', '2017-07-18', '2017-07-19',
               '2017-07-20', '2017-07-23', '2017-07-24', '2017-07-25',
               '2017-07-26', '2017-07-27', '2017-07-30', '2017-07-31'],
              dtype='datetime64[ns]', freq='C')


Mathematical operations on date object using custom business day :- 

from datetime import datetime
dt = datetime(2017,7,9)
dt

# datetime.datetime(2017, 7, 9, 0, 0)

dt + 1*b
# 
Timestamp('2017-07-11 00:00:00')

