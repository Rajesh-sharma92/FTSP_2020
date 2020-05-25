# Using Pandas Index :- 

import pandas as pd

url = 'http://bit.ly/drinksbycountry'

df = pd.read_csv(url)

df.head()

# To get the Index of the DataFrames.

df.index   # RangeIndex(start=0, stop=193, step=1)

# The index is from 0 to 193 (0, 1, 2, 3, 4... 193).


df.columns  # To get the Columns Names.
-------------
Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings',
       'total_litres_of_pure_alcohol', 'continent'],
      dtype='object')


# index is not part of the DataFrame.

df.shape # (193, 6)



# rarely people leave columns without headers.

url2 = 'http://bit.ly/movieusers'

df= pd.read_csv(url2 , delimiter='|' , header=None)

df.head()

cols = ['Number' , 'Age' , 'Sex' , 'Job' , 'ID_No']

df = pd.read_csv(url2 , names = cols , delimiter = '|' , header = None)

df.head()
------------------
   Number  Age Sex         Job  ID_No
0       1   24   M  technician  85711
1       2   53   F       other  94043
2       3   23   M      writer  32067
3       4   24   M  technician  43537
4       5   33   F       other  15213



Q.1.  What are indexes for ?

1) Identification
2) Selection
3) Alignment


1. Identification

# you can identify what rows we are working with here.

url = 'http://bit.ly/drinksbycountry'

df = pd.read_csv(url)

df[df['continent'] == 'South America'].head()
------------------------
     country  beer_servings  ...  total_litres_of_pure_alcohol      continent
6   Argentina            193  ...                           8.3  South America
20    Bolivia            167  ...                           3.8  South America
23     Brazil            245  ...                           7.2  South America
35      Chile            130  ...                           7.6  South America
37   Colombia            159  ...                           4.2  South America


2. Selection

# .loc method to retrieve element/cell.

df.loc[23 , 'beer_servings']  # 245


df.loc[6 , 'beer_servings']  # 193


# inplace=True makes the change 
# sets the index to 'country'

df.shape # (193, 6)

df.set_index('country' , inplace = True)

df.shape # (193, 5)

df.head()
--------------
             beer_servings  ...  continent
country                     ...           
Afghanistan              0  ...       Asia
Albania                 89  ...     Europe
Algeria                 25  ...     Africa
Andorra                245  ...     Europe
Angola                 217  ...     Africa

df.index # It shows the Index Names.

print(len(df.index)) # 193

# country is no longer one of the columns.

df.columns
------------------
Index(['beer_servings', 'spirit_servings', 'wine_servings',
       'total_litres_of_pure_alcohol', 'continent'],
      dtype='object')


# we can select based on country instead of a number 
# we can select more easily by setting a meaningful index

df.loc['Brazil' ,'beer_servings'] # 245


df.loc['Brazil' ,'wine_servings'] # 16


'country' is the name of the index
We can clear this out

# clearing index name.

df.index.name = None

df.head()
----------------
             beer_servings  ...  continent
Afghanistan              0  ...       Asia
Albania                 89  ...     Europe
Algeria                 25  ...     Africa
Andorra                245  ...     Europe
Angola                 217  ...     Africa



# say you prefer to use the default index and you want back the column of countries.

df.index.name = 'country'
df.reset_index(inplace=True)
df.head()
-------------
       country  beer_servings  ...  total_litres_of_pure_alcohol  continent
0  Afghanistan              0  ...                           0.0       Asia
1      Albania             89  ...                           4.9     Europe
2      Algeria             25  ...                           0.7     Africa
3      Andorra            245  ...                          12.4     Europe
4       Angola            217  ...                           5.9     Africa


df.shape  # (193, 6)

df.describe()
------------------------
       beer_servings  ...  total_litres_of_pure_alcohol
count     193.000000  ...                    193.000000
mean      106.160622  ...                      4.717098
std       101.143103  ...                      3.773298
min         0.000000  ...                      0.000000
25%        20.000000  ...                      1.300000
50%        76.000000  ...                      4.200000
75%       188.000000  ...                      7.200000
max       376.000000  ...                     14.400000



print(type(df.describe())) # <class 'pandas.core.frame.DataFrame'>
# you can see this is a DataFrame so we can interact with it accordingly


df.describe().index
---------------------------
Index(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], dtype='object')


df.describe().columns
--------------------
Index(['beer_servings', 'spirit_servings', 'wine_servings',
       'total_litres_of_pure_alcohol'],
      dtype='object')


# .loc is a DataFrame method
# format of .loc
# .loc['index_name_or_number', 'column_name]

df.describe().loc['25%' , 'beer_servings'] #20.0


3. Alignment

df.head()
----------------
      country  beer_servings  ...  total_litres_of_pure_alcohol  continent
0  Afghanistan              0  ...                           0.0       Asia
1      Albania             89  ...                           4.9     Europe
2      Algeria             25  ...                           0.7     Africa
3      Andorra            245  ...                          12.4     Europe
4       Angola            217  ...                           5.9     Africa


df['continent'].head()
-----------------------
0      Asia
1    Europe
2    Africa
3    Europe
4    Africa
Name: continent, dtype: object


df.set_index('country', inplace=True)

df.head()
-----------
             beer_servings  ...  continent
country                     ...           
Afghanistan              0  ...       Asia
Albania                 89  ...     Europe
Algeria                 25  ...     Africa
Andorra                245  ...     Europe
Angola                 217  ...     Africa


df['continent'].head()
-----------------
country
Afghanistan      Asia
Albania        Europe
Algeria        Africa
Andorra        Europe
Angola         Africa
Name: continent, dtype: object
 
print(type(df['continent']))  # <class 'pandas.core.series.Series'>

df['continent'].value_counts()
-------------------
Africa           53
Europe           45
Asia             44
North America    23
Oceania          16
South America    12
Name: continent, dtype: int64


print(type(df['continent'].value_counts())) # <class 'pandas.core.series.Series'>


df['continent'].value_counts().values
# array([53, 45, 44, 23, 16, 12], dtype=int64)

# we can use the index to select values from the series
# this is similar to .loc for DataFrame
# because series does not have multiple columns, we can do this
df['continent'].value_counts()['Africa'] # 53


# sort based on values in the Series
df.continent.value_counts().sort_values()
---------------------
South America    12
Oceania          16
North America    23
Asia             44
Europe           45
Africa           53
Name: continent, dtype: int64


# sort index based on ascending order
df['continent'].value_counts().sort_index()
------------------
Africa           53
Asia             44
Europe           45
North America    23
Oceania          16
South America    12
Name: continent, dtype: int64


# creating a a pandas series
people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name='population')

people
------------
Albania    3000000
Andorra      85000
Name: population, dtype: int64

df['beer_servings'].head()
---------------------
country
Afghanistan      0
Albania         89
Algeria         25
Andorra        245
Angola         217
Name: beer_servings, dtype: int64


# you can do math based on shared index
df['beer_servings'] * people


# axis=1, column concatenation
# beauty of automatic alignment using index

pd.concat([df, people], axis=1).head()
------------------

             beer_servings  spirit_servings  ...  continent  population
Afghanistan              0                0  ...       Asia         NaN
Albania                 89              132  ...     Europe   3000000.0
Algeria                 25                0  ...     Africa         NaN
Andorra                245              138  ...     Europe     85000.0
Angola                 217               57  ...     Africa         NaN





