# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:29:42 2020

@author: Rajesh
"""
import pandas as pd

df = pd.read_csv(r'E:\CodeBasics_Pandas\Pandas_CSV_CB\aapl_no_dates.csv')
df.head()
------
     Open    High     Low   Close    Volume
0  153.17  153.33  152.22  153.18  16404088
1  153.58  155.45  152.89  155.45  27770715
2  154.34  154.45  153.46  153.93  25331662
3  153.90  155.81  153.78  154.45  26624926
4  155.02  155.98  154.48  155.37  21069647

rng = pd.date_range(start='04/01/2020',end='04/30/2020',freq='B')
# It is working fine.

DatetimeIndex(['2020-04-01', '2020-04-02', '2020-04-03', '2020-04-06',
               '2020-04-07', '2020-04-08', '2020-04-09', '2020-04-10',
               '2020-04-13', '2020-04-14', '2020-04-15'],
              dtype='datetime64[ns]', freq='B')



df.set_index(rng,inplace=True) # It will make the changes into original dataset.

# If we want to plot some of the Chart.
%matplotlib inline
df.Close.plot()

df.Open['2020-04-01'] # 153.17

df.Open['2020-04-01':'2020-04-10']
2020-04-01    153.17
2020-04-02    153.58
2020-04-03    154.34
2020-04-06    153.90
2020-04-07    155.02
2020-04-08    155.25
2020-04-09    155.19
2020-04-10    145.74

# If we do the frequency as the Day wise then it will be including the Holidays also.
df.asfreq('D',method='pad').head()
-------------
2020-04-01  153.17  153.33  152.22  153.18  16404088
2020-04-02  153.58  155.45  152.89  155.45  27770715
2020-04-03  154.34  154.45  153.46  153.93  25331662
2020-04-04  154.34  154.45  153.46  153.93  25331662
2020-04-05  154.34  154.45  153.46  153.93  25331662

# If we want to display the Timing also then we will using all these things.
df.asfreq('H',method='pad').head()
------------
                       Open    High     Low   Close    Volume
2020-04-01 00:00:00  153.17  153.33  152.22  153.18  16404088
2020-04-01 01:00:00  153.17  153.33  152.22  153.18  16404088
2020-04-01 02:00:00  153.17  153.33  152.22  153.18  16404088
2020-04-01 03:00:00  153.17  153.33  152.22  153.18  16404088
2020-04-01 04:00:00  153.17  153.33  152.22  153.18  16404088


# NOTE :- Here we can use any kind of frequencies as per the business requirement.
# We will be getting all those information on Pandas Website on Google.

# If we want to get the all information as per hourly based.
rng= pd.date_range(start='01/01/2020',periods=72,freq='H')
print(rng)

# '2020-01-01 00:00:00', '2020-01-01 01:00:00',

# How to get the Random Number into Machine Learning.
import numpy as np
ts = pd.Series(np.random.randint(1,10,len(rng)),index='rng')
ts.head()














