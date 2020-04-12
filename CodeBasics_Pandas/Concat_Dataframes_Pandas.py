# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:41:36 2020

@author: Rajesh
"""
# How to concatenated the two or more DataFrames.

import pandas as pd

India_weather = pd.DataFrame({'city': ['mumbai','delhi','bangalore'],
                 'temperature': [32,45,30],
                 'humidity': [80,60,78]
        })


US_weather = pd.DataFrame({'city': ['newyork','chicago','orilando'],
                 'temperature': [21,14,35],
                 'humidity': [68,65,75]
        })

# Here we will be combined both the DataFrames in Pandas by using the Concat()
# and it may more the 2 dataframes.

df = pd.concat([India_weather,US_weather])
print(df)
***********
       city  temperature  humidity
0     mumbai           32        80
1      delhi           45        60
2  bangalore           30        78
0    newyork           21        68
1    chicago           14        65
2   orilando           35        75

# Here we are not getting the perfect Index as numbers.
df = pd.concat([India_weather,US_weather] ,ignore_index=True)
print(df)
**********
        city  temperature  humidity
0     mumbai           32        80
1      delhi           45        60
2  bangalore           30        78
3    newyork           21        68
4    chicago           14        65
5   orilando           35        75

df = pd.concat([India_weather,US_weather] ,keys=['India','US'])
print(df)
*************
            city  temperature  humidity
India 0     mumbai           32        80
      1      delhi           45        60
      2  bangalore           30        78
US    0    newyork           21        68
      1    chicago           14        65
      2   orilando           35        75


df.loc['India']
*********
       city  temperature  humidity
0     mumbai           32        80
1      delhi           45        60
2  bangalore           30        78


df.loc['US']
***********
      city  temperature  humidity
0   newyork           21        68
1   chicago           14        65
2  orilando           35        75


# Here wa have some of the others use of the pandas.

temperature_df = pd.DataFrame({'city': ['mumbai','delhi','bangalore'],
                 'temperature': [32,45,30] })


windspeed_df = pd.DataFrame({'city': ['mumbai','delhi','bangalore'],
                 'windspeed': [7,15,10] })


df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)
**********
      city  temperature       city  windspeed
0     mumbai           32     mumbai          7
1      delhi           45      delhi         15
2  bangalore           30  bangalore         10


# If we don't have one city like bangalore information.
temperature_df = pd.DataFrame({'city': ['mumbai','delhi','bangalore'],
                 'temperature': [32,45,30] })

print(temperature_df)
-------------------------
        city  temperature
0     mumbai           32
1      delhi           45
2  bangalore           30


windspeed_df = pd.DataFrame({'city': ['mumbai','delhi'],
                 'windspeed': [7,15] })

print(windspeed_df)
----------------------
     city  windspeed
0  mumbai          7
1   delhi         15


df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)
-------------
      city  temperature    city  windspeed
0     mumbai           32  mumbai        7.0
1      delhi           45   delhi       15.0
2  bangalore           30     NaN        NaN


temperature_df = pd.DataFrame({'city': ['mumbai','delhi','bangalore'],
                 'temperature': [32,45,30]}, index=[0,1,2])

windspeed_df = pd.DataFrame({'city': ['delhi','mumbai'],
                 'windspeed': [7,15]}, index=[1,0])

df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)
---------------      city  temperature    city  windspeed
0     mumbai           32  mumbai       15.0
1      delhi           45   delhi        7.0
2  bangalore           30     NaN        NaN


# How to create the new series in Pandas.
s = pd.Series(['humit','dry','rain'],name='event')
print(s)
----------
0    humit
1      dry
2     rain

df = pd.concat([temperature_df,s], axis=1)
print(df)
-------------
       city  temperature  event
0     mumbai           32  humit
1      delhi           45    dry
2  bangalore           30   rain
















