# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:42:16 2020

@author: Rajesh
"""
1) Find maximum temperature at each city.

2) Find avarage wind speed for every city.


import pandas as pd
import numpy as np

df = pd.read_csv('E:\CodeBasics_Pandas\Pandas_CSV_CB\weather_by_cities.csv')
df.head()
*************
       day      city  temperature  windspeed  event
0  1/1/2017  new york           32          6   Rain
1  1/2/2017  new york           36          7  Sunny
2  1/3/2017  new york           28         12   Snow
3  1/4/2017  new york           33          7  Sunny
4  1/1/2017    mumbai           90          5  Sunny

# Now we will do the groupny() method of pandas.
g = df.groupby('city')
print(g)

# We are using the python Iterator concept here.
for city,city_df in g:
    print(city)
    print(city_df)
    
*********************    
mumbai
        day    city  temperature  windspeed  event
4  1/1/2017  mumbai           90          5  Sunny
5  1/2/2017  mumbai           85         12    Fog
6  1/3/2017  mumbai           87         15    Fog
7  1/4/2017  mumbai           92          5   Rain
new york
        day      city  temperature  windspeed  event
0  1/1/2017  new york           32          6   Rain
1  1/2/2017  new york           36          7  Sunny
2  1/3/2017  new york           28         12   Snow
3  1/4/2017  new york           33          7  Sunny
paris
         day   city  temperature  windspeed   event
8   1/1/2017  paris           45         20   Sunny
9   1/2/2017  paris           50         13  Cloudy
10  1/3/2017  paris           54          8  Cloudy
11  1/4/2017  paris           42         10  Cloudy

# If we want to get the specific data.
g.get_group('mumbai')
***************
        day    city  temperature  windspeed  event
4  1/1/2017  mumbai           90          5  Sunny
5  1/2/2017  mumbai           85         12    Fog
6  1/3/2017  mumbai           87         15    Fog
7  1/4/2017  mumbai           92          5   Rain

# How to get the maximum Temperature.
g.max()
*******
            day     temperature    windspeed  event
city                                             
mumbai    1/4/2017           92         15  Sunny
new york  1/4/2017           36         12  Sunny
paris     1/4/2017           54         20  Sunny

# For single city.
df[df['city']=='mumbai'].max()
**************
day            1/4/2017
city             mumbai
temperature          92
windspeed            15
event             Sunny

# To get the mean or average of the cities.
g.mean()
********
          temperature  windspeed
city                            
mumbai          88.50       9.25
new york        32.25       8.00
paris           47.75      12.75

# If we want to get the details of the all cities at the same time.
g.describe() # It will be working as combine the values.


# We can use like this also.
df[df['city']=='mumbai'].describe()
******
     temperature  windspeed
count     4.000000   4.000000
mean     88.500000   9.250000
std       3.109126   5.057997
min      85.000000   5.000000
25%      86.500000   5.000000
50%      88.500000   8.500000
75%      90.500000  12.750000
max      92.000000  15.000000


# We will the some the graph here.
%matplotlib inline
g.plot()

