# Pandas Sorting :- 

import pandas as pd

url = 'http://bit.ly/imdbratings'

movies = pd.read_csv(url)

movies.head()

movies.columns
-----------------
Index(['star_rating', 'title', 'content_rating', 'genre',
       'duration','actors_list'] , dtype='object')



# sort using sort_values
movies.sort_values('star_rating')

movies.sort_values('title')

movies.sort_values('duration')

# sort with numbers first then alphabetical order

movies.title.sort_values()

movies.star_rating.sort_values()

movies.duration.sort_values()

# alternative sorting # Recommanded to do it by this way always.

movies['title']

movies['title'].sort_values().head()
---------------
542     (500) Days of Summer
5               12 Angry Men
201         12 Years a Slave
698                127 Hours
110    2001: A Space Odyssey
Name: title, dtype: object

# returns a series.

print(type(movies['title'].sort_values()))
# <class 'pandas.core.series.Series'>


# Sort Column 
# How to sort the Columns into Reverse or Descending order.
# sort in ascending=False
# this does not affect the underlying data
movies.title.sort_values(ascending=False).head()
----------
864               [Rec]
526                Zulu
615          Zombieland
677              Zodiac
955    Zero Dark Thirty
Name: title, dtype: object


movies['title'].sort_values(ascending=True).head()
-------------------------
542     (500) Days of Summer
5               12 Angry Men
201         12 Years a Slave
698                127 Hours
110    2001: A Space Odyssey
Name: title, dtype: object


movies['title'].sort_values(ascending=False).head()
-----------------
864               [Rec]
526                Zulu
615          Zombieland
677              Zodiac
955    Zero Dark Thirty
Name: title, dtype: object

movies['duration'].sort_values().head()
--------------------
389    64
338    66
258    67
293    68
88     68
Name: duration, dtype: int64

# NOTE :- Default Ascending = True only and It will gives the 
# Ascending values only from DF.

movies['duration'].sort_values(ascending=False).head()
-----------------
476    242
157    238
78     229
142    224
445    220
Name: duration, dtype: int64


# Sort DataFrame using a particular .

movies.sort_values('actors_list')

movies.sort_values('actors_list' , ascending = False)


  ''' Sorting a DataFrame using multiple columns '''
    
# create list of columns
# sort using content_rating
# then within content_rating, sort by duration

columns = ['content_rating', 'duration']

# sort column
movies.sort_values(columns).head()


movies.columns

col_list = ['star_rating','duration']

movies.sort_values(col_list).head()[['star_rating','duration']]
------------------
    star_rating  duration
938          7.4        75
948          7.4        86
966          7.4        87
947          7.4        89
971          7.4        90



col_list = ['genre','duration']

movies.sort_values(col_list).head()[['genre','duration']]
------------------
     genre  duration
533  Action        80
633  Action        92
455  Action        93
685  Action        93
744  Action        94


movies.sort_values(col_list).tail()[['genre','duration']]
------------------
       genre  duration
421  Western       135
263  Western       141
6    Western       161
59   Western       165
26   Western       175





