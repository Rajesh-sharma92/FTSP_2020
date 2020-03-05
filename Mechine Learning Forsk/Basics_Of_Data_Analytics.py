# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:55:15 2020

@author: Rajesh
"""

Pandas :- panel data set.

# How to import pandas into our program.
# Pandas is the very powerful libraries in the python.

import pandas as pd

ps = pd.Series(['a','b','c','d'])
print(ps)

******* Result *******
0    a
1    b
2    c
3    d
dtype: object

ts = pd.Series(('a','b','c','d'))
print(ts)

******* Result *******
0    a
1    b
2    c
3    d
dtype: object

data = pd.Series([10,20,30,40,50])
print(data)
type(data) # pandas.core.series.Series

0    10
1    20
2    30
3    40
4    50
dtype: int64
----------------------------------------------------------------------------------------------------
NOTE :- We can see that Series is the one-dimensional data type.
-------------------------------------------------------------------------------------------
''' How to customized the Indexes '''
----------------------------------------
data = pd.Series(['Python','Mechine Learning','Deep Learning','Analytics'])
print(data)

0              Python
1    Mechine Learning
2       Deep Learning
3           Analytics


data = pd.Series(['Python','Mechine Learning','Deep Learning','Analytics'] , index=[100,101,102,103])
print(data)

100              Python
101    Mechine Learning
102       Deep Learning
103           Analytics
-----------------------------------------------------------------------------------------------------------


import pandas as pd
df = pd.read_csv('E:\Forsk Pandas\CSV files\Salaries.csv')
print(df)

df.columns
['rank', 'discipline', 'phd', 'service', 'sex', 'salary']

---------------------------------------------------------------------------------------------
df[(df['service']==49) & (df['sex']=='Male')]

rank discipline   phd  service   sex    salary
0  Prof          B  56.0       49  Male  186960.0

df[(df['salary']==88000) & (df['sex']=='Male')]

      rank discipline  phd  service   sex   salary
12  AsstProf          B  1.0        0  Male  88000.0

df[(df['rank']=='Prof')].count()

ank          46
discipline    46
phd           45
service       46
sex           46
salary        45

df[(df['rank']=='Prof')].count()['rank'] # 46

df['salary'].count() # 76

df['salary'].value_counts(normalize = True) # 71

df[df['salary'].isnull()]

        rank discipline   phd  service   sex  salary
7       Prof          A  18.0       18  Male     NaN
28  AsstProf          B   7.0        2  Male     NaN

df.count()

rank          78
discipline    78
phd           76
service       78
sex           78
salary        76
dtype: int64

df[df['salary'].isnull()].count()['rank'] # 2

----------------------------------------------------------------------------------------------------------
df[(df['rank']=='Prof')].count()['rank'] # 46

df[(df['rank']=='AsstProf')].count()['rank'] # 19

df[(df['rank']=='AssocProf')].count()['rank'] # 13

df.groupby('rank').max()
df.groupby('salary').max()
df.groupby('salary').count()

df.groupby(['rank','sex']).max()

df.columns

df.groupby('discipline').max()

            rank   phd  service   sex    salary
discipline                                     
A           Prof  51.0       51  Male  155865.0
B           Prof  56.0       49  Male  186960.0

df.groupby('discipline').min()

                rank  phd  service     sex   salary
discipline                                          
A           AssocProf  2.0        0  Female  57800.0
B           AssocProf  1.0        0  Female  71065.0


df.groupby('discipline').count()

          rank  phd  service  sex  salary
discipline                                 
A             36   36       36   36      35
B             42   40       42   42      41


df[(df['salary'] > 150000) & (df['sex']=='Male')]

    rank discipline   phd  service   sex    salary
0   Prof          B  56.0       49  Male  186960.0
13  Prof          B   NaN       33  Male  162200.0
14  Prof          B  25.0       19  Male  153750.0
15  Prof          B  17.0        3  Male  150480.0
19  Prof          A  29.0       27  Male  150500.0
27  Prof          A  45.0       43  Male  155865.0
31  Prof          B  22.0       21  Male  155750.0

df[(df['salary'] > 150000) & (df['sex']=='Female')]

  rank discipline   phd  service     sex    salary
44  Prof          B  23.0       19  Female  151768.0
72  Prof          B  24.0       15  Female  161101.0

df.shape # (78, 6)

df.ndim # 2

df.size # 468

df.head() # First 5 records from database file.

df.tail() # Last 5 records from database file.

df.index # RangeIndex(start=0, stop=78, step=1)

df.columns
Index(['rank', 'discipline', 'phd', 'service', 'sex', 'salary'], dtype='object')

df.dtypes

rank           object
discipline     object
phd           float64
service         int64
sex            object
salary        float64
dtype: object

df.values  # It provides all values into dataframe.

dv = df.values
for item in dv:
    print(item)
    
df.loc[:1] # It includes from start to end range and last number also will be included.
    
  rank discipline   phd  service   sex    salary
0  Prof          B  56.0       49  Male  186960.0
1  Prof          A  12.0        6  Male   93000.0

df.loc[10:20 , ['rank','sex']]

df[1:4] # 4th line will be exclusive in the data.

  rank discipline   phd  service   sex    salary
1  Prof          A  12.0        6  Male   93000.0
2  Prof          A  23.0       20  Male  110515.0
3  Prof          A  40.0       31  Male  131205.0

df.loc[1:4] # 4th line will be Inclusive in the data.
  rank discipline   phd  service   sex    salary
1  Prof          A  12.0        6  Male   93000.0
2  Prof          A  23.0       20  Male  110515.0
3  Prof          A  40.0       31  Male  131205.0
4  Prof          B  20.0       18  Male  104800.0

df.loc[1:4 , 'rank']
1    Prof
2    Prof
3    Prof
4    Prof

df.loc[1:4 , ['rank','sex']]

   rank   sex
1  Prof  Male
2  Prof  Male
3  Prof  Male
4  Prof  Male

df['rank'].unique()

array(['Prof', 'AssocProf', 'AsstProf'], dtype=object)

df_list = df['rank'].unique().tolist()
print(df_list)
['Prof', 'AssocProf', 'AsstProf']

df.iloc[1:4]
  rank discipline   phd  service   sex    salary
1  Prof          A  12.0        6  Male   93000.0
2  Prof          A  23.0       20  Male  110515.0
3  Prof          A  40.0       31  Male  131205.0

df['rank'].iloc[1:4]

1    Prof
2    Prof
3    Prof

df['rank'].unique().tolist().

['Prof', 'AssocProf', 'AsstProf']

df['discipline'].unique().tolist()

['B', 'A']

df['sex'].unique().tolist()

['Male', 'Female']

df_list = df['salary'].unique().tolist()

df_list






































































































































