# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:25:40 2020

@author: Rajesh
"""

import pandas as pd

df = pd.read_csv('E:\CodeBasics_Pandas\Pandas_CSV_CB\weather.csv')

df.head()
------------      date      city  temperature  humidity
0  5/1/2017  new york           65        56
1  5/2/2017  new york           66        58
2  5/3/2017  new york           68        60
3  5/1/2017    mumbai           75        80
4  5/2/2017    mumbai           78        83

df.shape # (9, 4)

df.pivot(index='date',columns='city')
-------------
         temperature                 humidity                
city         beijing mumbai new york  beijing mumbai new york
date                                                         
5/1/2017          80     75       65       26     80       56
5/2/2017          77     78       66       30     83       58
5/3/2017          79     82       68       35     85       60

# If we want to take only humidity.

df.pivot(index='date',columns='city',values='humidity')
-----------------
city      beijing  mumbai  new york
date                               
5/1/2017       26      80        56
5/2/2017       30      83        58
5/3/2017       35      85        60

 # If we takes index is the humidity then.
df.pivot(index='humidity',columns='city')
-----------------
             date                     temperature                
city       beijing    mumbai  new york     beijing mumbai new york
humidity                                                          
26        5/1/2017       NaN       NaN        80.0    NaN      NaN
30        5/2/2017       NaN       NaN        77.0    NaN      NaN
35        5/3/2017       NaN       NaN        79.0    NaN      NaN
56             NaN       NaN  5/1/2017         NaN    NaN     65.0
58             NaN       NaN  5/2/2017         NaN    NaN     66.0
60             NaN       NaN  5/3/2017         NaN    NaN     68.0
80             NaN  5/1/2017       NaN         NaN   75.0      NaN
83             NaN  5/2/2017       NaN         NaN   78.0      NaN
85             NaN  5/3/2017       NaN         NaN   82.0      NaN

-------------------------------------------------------------------------------------------------

df = pd.read_csv('E:\CodeBasics_Pandas\Pandas_CSV_CB\weather2.csv')
print(df)
---------------
       date      city  temperature  humidity
0  5/1/2017  new york           65        56
1  5/1/2017  new york           61        54
2  5/2/2017  new york           70        60
3  5/2/2017  new york           72        62
4  5/1/2017    mumbai           75        80
5  5/1/2017    mumbai           78        83
6  5/2/2017    mumbai           82        85
7  5/2/2017    mumbai           80        26

df.pivot_table(index='city',columns='date')
---------
        humidity          temperature         
date     5/1/2017 5/2/2017    5/1/2017 5/2/2017
city                                           
mumbai       81.5     55.5        76.5     81.0
new york     55.0     61.0        63.0     71.0

# If we want then we can take the aggerateed values also.
df.pivot_table(index='city',columns='date',aggfunc='sum')
-----------------
         humidity          temperature         
date     5/1/2017 5/2/2017    5/1/2017 5/2/2017
city                                           
mumbai        163      111         153      162
new york      110      122         126      142


df.pivot_table(index='city',columns='date',aggfunc='count')
----------------
         humidity          temperature         
date     5/1/2017 5/2/2017    5/1/2017 5/2/2017
city                                           
mumbai          2        2           2        2
new york        2        2           2        2

df.pivot_table(index='city',columns='date',aggfunc='diff')
------------
   humidity  temperature
1        -2           -4
3         2            2
5         3            3
7       -59           -2

df.pivot_table(index='city',columns='date',aggfunc='mean')
--------------
        humidity          temperature         
date     5/1/2017 5/2/2017    5/1/2017 5/2/2017
city                                           
mumbai       81.5     55.5        76.5     81.0
new york     55.0     61.0        63.0     71.0


df.pivot_table(index='city',columns='date',margins=True)
------------
         humidity                 temperature                 
date     5/1/2017 5/2/2017    All    5/1/2017 5/2/2017     All
city                                                          
mumbai      81.50    55.50  68.50       76.50     81.0  78.750
new york    55.00    61.00  58.00       63.00     71.0  67.000
All         68.25    58.25  63.25       69.75     76.0  72.875

-----------------------------------------------------------------------------------------------------------

df = pd.read_csv('E:\CodeBasics_Pandas\Pandas_CSV_CB\weather3.csv')
print(df)
--------------
        date      city  temperature  humidity
0   5/1/2017  new york           65        56
1   5/2/2017  new york           61        54
2   5/3/2017  new york           70        60
3  12/1/2017  new york           30        50
4  12/2/2017  new york           28        52
5  12/3/2017  new york           25        51

print(type(df['date'][0])) # <class 'str'>

pd._libs.tslib.Timestamp # pandas._libs.tslibs.timestamps.Timestamp


df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')


