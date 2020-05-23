# Examining Dataset :- 

 ''' Reading subset of columns or rows '''
 
import pandas as pd

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)

df.columns 
------------------
Index(['City', 'Colors Reported', 'Shape Reported',
       'State', 'Time'], dtype='object')

# reference Columns by using String

cols = ['City','State']

df = pd.read_csv(url , usecols = cols)

df.head()
---------------
                   City State
0                Ithaca    NY
1           Willingboro    NJ
2               Holyoke    CO
3               Abilene    KS
4  New York Worlds Fair    NY


# reference Columns by using position (Integer).

cols2 = [0,4]

df = pd.read_csv(url , usecols = cols2)

df.head()
--------------
                   City             Time
0                Ithaca   6/1/1930 22:00
1           Willingboro  6/30/1930 20:00
2               Holyoke  2/15/1931 14:00
3               Abilene   6/1/1931 13:00
4  New York Worlds Fair  4/18/1933 19:00


# If you only want certain number of rows.
# We have nrows = n.

df = pd.read_csv(url , nrows = 5)

df

df['City']
------------
0                  Ithaca
1             Willingboro
2                 Holyoke
3                 Abilene
4    New York Worlds Fair
Name: City, dtype: object

df.count()
---------------
City               5
Colors Reported    0
Shape Reported     5
State              5
Time               5
dtype: int64


 ''' Iterating through a Series and DataFrame '''

for city in df['City']:
    print(city)
--------------------
Ithaca
Willingboro
Holyoke
Abilene
New York Worlds Fair


for mins in df['Time']:
    print(mins)
------------------
6/1/1930 22:00
6/30/1930 20:00
2/15/1931 14:00
6/1/1931 13:00
4/18/1933 19:00


# pandas method
# you can grab index and row.

for index,rows in df.iterrows():
    print(index , df['City'] , df['State']) # Working
    

for i,j in df.iterrows():
    print(df['City'] , df['State'])
    
for i in df.iterrows():
    print(df['Time'].head())


    
 ''' Drop non-numeric column in a DataFrame '''
 
url = 'http://bit.ly/drinksbycountry'

df = pd.read_csv(url)

# you have 2 non-numeric columns
df.dtypes 
 
 
import numpy as np

df.select_dtypes(include=[np.number]).dtypes
beer_servings                     int64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
dtype: object



''' Passing arguments, when to use list or string ''' 
 
df.describe(include = 'all').count()
 
 
# here you pass a list
# use shift + tab to know what arguments to pass in.

list_include = ['object', 'float64']

df.describe(include = list_include).head()
 
 
df.describe(include = 'int64')
---------------
     beer_servings  spirit_servings  wine_servings
count     193.000000       193.000000     193.000000
mean      106.160622        80.994819      49.450777
std       101.143103        88.284312      79.697598
min         0.000000         0.000000       0.000000
25%        20.000000         4.000000       1.000000
50%        76.000000        56.000000       8.000000
75%       188.000000       128.000000      59.000000
max       376.000000       438.000000     370.000000 
 
 
 
    
    
    