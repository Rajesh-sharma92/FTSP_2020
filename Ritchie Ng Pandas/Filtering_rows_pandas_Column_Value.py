# Filtering rows of a pandas DataFrame by column value :-

import pandas as pd

url = 'http://bit.ly/imdbratings'

df = pd.read_csv(url)

df.head()

df.columns

df.shape # (979, 6)

# booleans
print(type(True)) # bool
print(type(False)) # bool

Q.1. We want to create a list of booleans with the same number of 
     rows as the movies' DataFrame

 True if duration > 200
 False if otherwise

# How to create Empty list.
booleans = [] # Empty list

# Apply the for each loop now.
 
for length in df['duration']:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)
        
booleans[7:12]    
------------
[True, False, False, False, False]

# To check the length of Booleans.
print(len(booleans)) # 979


# To convert booleans into a Pandas series.

is_long = pd.Series(booleans)

is_long.head()
-------------------
0    False
1    False
2     True
3    False
4    False
dtype: bool

df.columns
---------------
Index(['star_rating', 'title', 'content_rating', 'genre', 
       'duration',  'actors_list'] , dtype='object')

df['genre'].head()
--------------------
0     Crime
1     Crime
2     Crime
3    Action
4     Crime
Name: genre, dtype: object


# this pulls out duration >= 200mins.

df[is_long].head() # It will work



 '''  Faster method without a for loop  '''

# this line of code replaces the for loop
# when you use a series name using pandas and use a comparison 
# operator, it will loop through each row.
 
is_long = movies['duration'] >= 200
is_long.head()
-----------
0    False
1    False
2     True
3    False
4    False
Name: duration, dtype: bool


df[is_long].head()


''' Even better way to simplify movies[is_long] '''


df[ df['duration'] >= 200 ].head() # it will working.




# Additional tip: we want to study the duration and only 
# the genre instead of all the columns

# this is a DataFrame, we use dot or bracket notation to get what we want
df[ df['duration'] >= 200]['genre'].head(10)
--------------------
2          Crime
7      Adventure
17         Drama
78         Crime
85     Adventure
142    Adventure
157        Drama
204    Adventure
445    Adventure
476        Drama
Name: genre, dtype: object



# NOTE :-  best practice is to use .loc instead of what
#      we did above by selecting columns.

df.loc[ df['duration'] >= 200 , 'genre'].head(10)
----------------
2          Crime
7      Adventure
17         Drama
78         Crime
85     Adventure
142    Adventure
157        Drama
204    Adventure
445    Adventure
476        Drama
Name: genre, dtype: object



'''  Applying multiple filter criter to a pandas DataFrame '''


import pandas as pd

url = 'http://bit.ly/imdbratings'

# Create movies DataFrame
df = pd.read_csv(url)

df.head()

df[ df['duration'] >= 200 ].head() # It will work 

df[ df['genre'] == 'Drama' ].head() # It will work 

# If we want the Condition like Print the Movies details that are 
# 200 mins more & should me Drama types.

# AND Condition Means Both should be Correct.
# AND = & 

df[(df['duration'] >= 200) & (df['genre'] == 'Drama')].head()


# OR Condition Means one should be Correct both of them.
# OR = |

df[(df['duration'] >= 200) |  (df['genre'] == 'Drama')].head()


Q.1. What if you want genres crime, drama, and action ?
Answer :- 

# Slow Method
df[ (df['genre'] == 'Crime') | (df['genre'] == 'Drama') |(df['genre'] == 'Action') ]


# Fast Method

film_list = ['Crime','Drama','Action']

df_film = df[df['genre'].isin(film_list)]

df_film.count()['genre'] # 538


# Fast Method

time_list = ['duration','star_rating']


df[time_list].head()
------------
  duration  star_rating
0       142          9.3
1       175          9.2
2       200          9.1
3       152          9.0
4       154          8.9






