# Making DataFrame Smaller and Faster :- 

import pandas as pd

url = 'http://bit.ly/drinksbycountry'

df = pd.read_csv(url)

df.head()
---------------
       country  beer_servings  ...  total_litres_of_pure_alcohol  continent
0  Afghanistan              0  ...                           0.0       Asia
1      Albania             89  ...                           4.9     Europe
2      Algeria             25  ...                           0.7     Africa
3      Andorra            245  ...                          12.4     Europe
4       Angola            217  ...                           5.9     Africa


df.info()
--------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 193 entries, 0 to 192
Data columns (total 6 columns):
country                         193 non-null object
beer_servings                   193 non-null int64
spirit_servings                 193 non-null int64
wine_servings                   193 non-null int64
total_litres_of_pure_alcohol    193 non-null float64
continent                       193 non-null object
dtypes: float64(1), int64(3), object(2)
memory usage: 9.2+ KB



object usually means there's a string
memory usage
DataFrame takes at least 9.2 kb of memory
It might be a lot more depending on what's in those object columns
In this case, they're just strings of countries and continents


# we can count the actual memory usage using the following command.

df.info(memory_usage = 'deep')
---------------------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 193 entries, 0 to 192
Data columns (total 6 columns):
country                         193 non-null object
beer_servings                   193 non-null int64
spirit_servings                 193 non-null int64
wine_servings                   193 non-null int64
total_litres_of_pure_alcohol    193 non-null float64
continent                       193 non-null object
dtypes: float64(1), int64(3), object(2)
memory usage: 30.5 KB



# we can check how much space each column is actually taking
# the numbers are in bytes, not kilobytes.

df.memory_usage(deep = True)
-------------------
Index                             128
country                         12588
beer_servings                    1544
spirit_servings                  1544
wine_servings                    1544
total_litres_of_pure_alcohol     1544
continent                       12332
dtype: int64

df.memory_usage()
-------------------------
Index                            128
country                         1544
beer_servings                   1544
spirit_servings                 1544
wine_servings                   1544
total_litres_of_pure_alcohol    1544
continent                       1544
dtype: int64

print(type(df.memory_usage(deep = True))) # <class 'pandas.core.series.Series'>


# since it is a series, we can use .sum()

df.memory_usage(deep = True).sum()  # 31224


# there are only 6 unique values of continent
# we can replace strings with digits to save space.

df['continent'].unique()
-----------------
array(['Asia', 'Europe', 'Africa', 'North America', 'South America',
       'Oceania'], dtype=object)
    

# To bring into the Sort form.
sorted(df['continent'].unique())    
-------------------------
['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']



df['continent'].head()    
--------------------
0      Asia
1    Europe
2    Africa
3    Europe
4    Africa
Name: continent, dtype: object


# converting continent from object to category 
# it stores the strings as integers.

df['continent'] = df['continent'].astype('category')

df['continent'].head()
-------------------------
0      Asia
1    Europe
2    Africa
3    Europe
4    Africa
Name: continent, dtype: category
Categories (6, object): [Africa, Asia, Europe, North America, Oceania, South America]


df.dtypes
-----------------
country                           object
beer_servings                      int64
spirit_servings                    int64
wine_servings                      int64
total_litres_of_pure_alcohol     float64
continent                       category
dtype: object


# .cat is similar to .str
# we can do more stuff after .cat
# we can see here how pandas represents the continents as integers

df['continent'].cat.codes.head()
-----------------
0    1
1    2
2    0
3    2
4    0
dtype: int8

# before this conversion, it was over 12332 bytes
# now it is 584 bytes

df.memory_usage(deep = True)
----------------
Index                             128
country                         12588
beer_servings                    1544
spirit_servings                  1544
wine_servings                    1544
total_litres_of_pure_alcohol     1544
continent                         744
dtype: int64


# we can convert country to a category too.

df['country'] = df['country'].astype('category')

df['country'].head()
--------------------
0    Afghanistan
1        Albania
2        Algeria
3        Andorra
4         Angola
Name: country, dtype: category
Categories (193, object): [Afghanistan, Albania, Algeria, Andorra, ..., Vietnam, Yemen, Zambia, Zimbabwe]

df.dtypes
---------------
country                         category
beer_servings                      int64
spirit_servings                    int64
wine_servings                      int64
total_litres_of_pure_alcohol     float64
continent                       category
dtype: object


# this is larger! 
# this is because we've too many categories.

df.memory_usage(deep = True)
-------------------
Index                             128
country                         18094
beer_servings                    1544
spirit_servings                  1544
wine_servings                    1544
total_litres_of_pure_alcohol     1544
continent                         744
dtype: int64

# now we've 193 digits
# it points to a lookup table with 193 strings!

df['country'].cat.categories


The key to converting to category is to ensure that there are few categories to save memory usage. 
If there are too many, we should not convert.


# passing a dictionary {} to the DataFrame method = 

id_list =[100, 101, 102, 103]

quality_list = ['good', 'very good', 'good', 'excellent']

df = pd.DataFrame({'ID': id_list, 'quality': quality_list })

df
------
   ID    quality
0  100       good
1  101  very good
2  102       good
3  103  excellent



# this sorts using alphabetical order
# but there is a logical ordering to these categories, we need to tell pandas there is a logical ordering

df.sort_values('quality')
--------------
    ID    quality
3  103  excellent
0  100       good
2  102       good
1  101  very good



# how do we tell pandas there is a logical order?

quality_list_ordered = ['good', 'very good', 'excellent']

df['quality'] = df.quality.astype('category', categories=quality_list_ordered, ordered=True)




# now it sorts using the logical order we defined
df.sort_values('quality')



# we can now use boolean conditions with this
# here we want all columns where the row > good

df.loc[df['quality'] > 'good', :]
--------------
   ID    quality
1  101  very good






