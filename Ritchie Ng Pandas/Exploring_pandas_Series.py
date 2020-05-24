# Exploring pandas Series :- 

import pandas as pd

url = 'http://bit.ly/imdbratings'

df = pd.read_csv(url)

df.head()


df.dtypes
----------------
star_rating       float64
title              object
content_rating     object
genre              object
duration            int64
actors_list        object

dtype: object


# We will be focusing on 2 columns

genre (object)
duration (integer)


# basic summary 

df['genre'].describe()
------------------
count       979
unique       16
top       Drama
freq        278
Name: genre, dtype: object


df['genre']
---------------
0          Crime
1          Crime
2          Crime
3         Action
4          Crime
   
974       Comedy
975    Adventure
976       Action
977       Horror
978        Crime
Name: genre, Length: 979, dtype: object


# frequency of different genres

df['genre'].value_counts().head()
-------------------
Drama        278
Comedy       156
Action       136
Crime        124
Biography     77
Name: genre, dtype: int64


df['genre'].count() # 979


# turn raw counts into percentages by Using (normalize=True)

df['genre'].value_counts(normalize = True).head()
Drama        0.283963
Comedy       0.159346
Action       0.138917
Crime        0.126660
Biography    0.078652
Name: genre, dtype: float64

# To check the Type of Genre details.

print(type(df['genre'].value_counts(normalize = True)))
# <class 'pandas.core.series.Series'>

# Hence we can use any Series method such as .head()

# Every time when you run a method, think of what other DataFrame or Series method we can chain


# finding out unique values.

df['genre'].unique()
-------------------
array(['Crime', 'Action', 'Drama', 'Western', 'Adventure', 'Biography',
       'Comedy', 'Animation', 'Mystery', 'Horror', 'Film-Noir', 'Sci-Fi',
       'History', 'Thriller', 'Family', 'Fantasy'], dtype=object)

df['genre'].nunique() # 16

df.columns


df['title'].unique()

df['title'].nunique() # 975


# crosstab is useful for explorng the data further.

pd.crosstab(df['genre'] , df['content_rating']).head()
------------------------------
content_rating  APPROVED   G  GP  NC-17  ...   R  TV-MA  UNRATED  X
genre                                    ...                       
Action                 3   1   1      0  ...  67      0        3  0
Adventure              3   2   0      0  ...  17      0        2  0
Animation              3  20   0      0  ...   5      0        1  0
Biography              1   2   1      0  ...  36      0        0  0
Comedy                 9   2   1      1  ...  73      0        4  1



df['duration'].describe()
-------------------------
count    979.000000
mean     120.979571
std       26.218010
min       64.000000
25%      102.000000
50%      117.000000
75%      134.000000
max      242.000000
Name: duration, dtype: float64


df['duration'].mean() # 120.97957099080695

df['duration'].max() # 242

df['duration'].min() # 64


df['duration'].value_counts().head()
-----------------------
112    23
113    22
102    20
101    20
129    19
Name: duration, dtype: int64



''' Visualization '''


data = df['duration']

data
--------------
0      142
1      175
2      200
3      152
4      154

974    116
975    118
976    138
977    114
978    126
Name: duration, Length: 979, dtype: int64


data.plot(kind='hist' , color='Blue')



data_counts = df['genre'].value_counts()

data_counts
--------------------
Drama        278
Comedy       156
Action       136
Crime        124
Biography     77
Adventure     75
Animation     62
Horror        29
Mystery       16
Western        9
Thriller       5
Sci-Fi         5
Film-Noir      3
Family         2
History        1
Fantasy        1
Name: genre, dtype: int64


data_counts.plot(kind='bar' , color = 'Red')

data_counts.plot(kind='bar' , color = 'Blue')

data_counts.plot(kind='bar' , color = 'pink')








