# Changing data type in Pandas :-

import pandas as pd

url = 'http://bit.ly/drinksbycountry'

df = pd.read_csv(url)

df.head()

df.columns

df.dtypes
--------------
country                          object
beer_servings                     int64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
continent                        object
dtype: object


# Data type summary

3 integers (int64)
1 floating (float64)
2 objects (object)


# Method 1: Change datatype after reading the csv

# to change use .astype() 

df['beer_servings'] = df['beer_servings'].astype(float)

df.dtypes
--------------
country                          object
beer_servings                   float64
spirit_servings                   int64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
continent                        object
dtype: object


# Method 2: Change datatype before reading the csv

df = pd.read_csv(url , dtype = {'spirit_servings' : float})

df.dtypes
-----------
country                          object
beer_servings                     int64
spirit_servings                 float64
wine_servings                     int64
total_litres_of_pure_alcohol    float64
continent                        object
dtype: object



# Check for this type of DataFrames.

url = 'http://bit.ly/chiporders'

df = pd.read_csv(url , delimiter = '\t')

df.head()

df.dtypes

order_id               int64
quantity               int64
item_name             object
choice_description    object
item_price            object
dtype: object

df['item_price'].head()

print(type('item_price')) # <class 'str'>


# The issue here is how pandas don't recognize item_price as
# a floating object

# we use .str to replace and then convert to float

df['item_price'] = df['item_price'].str.replace('$', '')

print(type('item_price'))


df['quantity'] = df['quantity'].astype(float)

df['quantity'].head()
-----------------
0    1.0
1    1.0
2    1.0
3    1.0
4    2.0
Name: quantity, dtype: float64

print(type(df['quantity']))
# <class 'pandas.core.series.Series'>


# we can now calculate the mean.

df['item_price'] = df['item_price'].str.replace('$', '')

df['item_price'].mean()


df['item_price'].head()


# To find out whether a column's row contains a certain string 
# by return True or False

df['item_name'].str.contains('Chicken').head()
------------------------
0    False
1    False
2    False
3    False
4     True
Name: item_name, dtype: bool


# convert to binary value.

df['item_name'].str.contains('Chicken').astype(int).head(10)
--------------------
0    0
1    0
2    0
3    0
4    1
5    1
6    0
7    0
8    0
9    0


df['item_name'].str.contains('Chicken').astype(float).head(6)
-----------------
0    0.0
1    0.0
2    0.0
3    0.0
4    1.0
5    1.0
Name: item_name, dtype: float64






