# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:21:35 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np

dataset = pd.read_csv('E:\CodeBasics_Pandas\Pandas_CSV_CB\weather_data.csv')
dataset.head()
****************
       day  temperature  windspeed  event
0  1/1/2017           32          6   Rain
1  1/2/2017       -99999          7  Sunny
2  1/3/2017           28     -99999   Snow
3  1/4/2017       -99999          7      0
4  1/5/2017           32     -99999   Rain

# NOTE :- It takes always 2 parameters like old to new value.
df = dataset.replace(-99999,np.NaN)
df.head()
************
        day  temperature  windspeed  event
0  1/1/2017         32.0        6.0   Rain
1  1/2/2017          NaN        7.0  Sunny
2  1/3/2017         28.0        NaN   Snow
3  1/4/2017          NaN        7.0      0
4  1/5/2017         32.0        NaN   Rain


# NOTE :- If there are more the one values and we need to replace the NaN then we will put 
# all the values into the list and replace with NaN and it will work it easily.
# like : df = dataset.replace([-99999,-88888] ,np.NaN)

NOTE :- If we want to replace the values for the specific columns like. 
NOTE :- For that we need to use the Dictionary concept.

df = dataset.replace({'temperature':-99999,
                 'windspeed':-99999,
                 'event':'0' }, np.NaN)

df.head()
************
       day  temperature  windspeed  event
0  1/1/2017         32.0        6.0   Rain
1  1/2/2017          NaN        7.0  Sunny
2  1/3/2017         28.0        NaN   Snow
3  1/4/2017          NaN        7.0    NaN
4  1/5/2017         32.0        NaN   Rain


# If we want to change the -99999 values to NaN & 'No Event' as 'Sunny'.
df = dataset.replace({-99999:np.NaN,
                 'No Event':'sunny'
        })

df.head()
**************
      day  temperature  windspeed  event
0  1/1/2017         32.0        6.0   Rain
1  1/2/2017          NaN        7.0  Sunny
2  1/3/2017         28.0        NaN   Snow
3  1/4/2017          NaN        7.0  sunny
4  1/5/2017         32.0        NaN   Rain

NOTE :- For an example our dataset contains the temeperature like 32F , 32C , windspeed like
6mph , 7mph and etc and we just want to replace the charaters from the dataset then we will for
concept like Regex experssion.



dataset.head()
*********************
       day temperature windspeed     event
0  1/1/2017         32F      6mph      Rain
1  1/2/2017      -99999      7mph     Sunny
2  1/3/2017          28    -99999      Snow
3  1/4/2017      -99999         7  No Event
4  1/5/2017         32C    -99999      Rain

df = dataset.replace('[A-Za-z]','',regex=True) # It will work but it will remove all the values from event col.
df.head()



# Here we will be using the Dictionary Concept like.
df = dataset.replace({'temperature':'[A-Za-z]',
                 'windspeed':'[A-Za-z]'}, '', regex=True)

df.head()
****************
        day temperature windspeed     event
0  1/1/2017          32         6      Rain
1  1/2/2017      -99999         7     Sunny
2  1/3/2017          28    -99999      Snow
3  1/4/2017      -99999         7  No Event
4  1/5/2017          32    -99999      Rain


NOTE :- Replacing list with another list:- 
-----------------------------------------

df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})

df
**********
         score  student
0  exceptional      rob
1      average     maya
2         good  parthiv
3         poor      tom
4      average   julian
5  exceptional    erica

df = df.replace(['poor', 'average','good','exceptional'],[1,2,3,4])

df
***********
   score  student
0      4      rob
1      2     maya
2      3  parthiv
3      1      tom
4      2   julian
5      4    erica

