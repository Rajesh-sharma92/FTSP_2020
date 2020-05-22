# Selecting Pandas Series :- 

# Selecting a pandas Series from a DataFrame
Q.1. What is a series ?
Answer :- 
It is a m x 1 vector.
m is the number of rows.
1 is the number of columns.
Each column in DataFrame is known as a pandas series.

import pandas as pd

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)

df.head()

# Now If we want to get the City details.

df.City.head() # Some times it won't be working properly.

df['City'].head() # It always works properly.

# 'City' is case-sensitive, you cannot use 'city'.

df['city'].head() # KeyError: 'city'

print(type(df['City']))
# <class 'pandas.core.series.Series'>

NOTE :- How do you select a column name with spacing between words?

# You cannot use method 2 (ufo.category_name)
# You have to use method 1 (ufo['category name'])

df['Colors Reported'].head() # It will be working.

Q.2. How do I create a new panda Series(Column) in a DataFrame ?
Answer :- 

# example of concatenating strings.
s1 = 'ab' + 'cd'
print(type(s1)) # <class 'str'>
print(s1) # abcd

# Created a new column called "Location" with a concatenation of "City" and "State"

df['Location'] = df['City'] + ',' + df['State']

df['Location']

df.columns

df.count()

df.head()




'''
Pandas commands ending with parentheses and those that do not :- 

'''
import pandas as pd

url = 'http://bit.ly/imdbratings'

movies = pd.read_csv(url)

# Looking at the first 5 rows of the DataFrame
movies.head()

# This will show descriptive statistics of numeric columns.
movies.describe()
------------
      star_rating    duration
count   979.000000  979.000000
mean      7.889785  120.979571
std       0.336069   26.218010
min       7.400000   64.000000
25%       7.600000  102.000000
50%       7.800000  117.000000
75%       8.100000  134.000000
max       9.300000  242.000000


movies.describe(include=['float64'])

movies.describe(include=['int64'])

# Finding out dimensionality of DataFrame.
movies.shape # (979, 6)

# Finding out data types of each columns
movies.dtypes

print(type(movies)) # <class 'pandas.core.frame.DataFrame'>


# As a Data Frame, it has certain methods and attributes

# Methods: with parentheses

Action-oriented

movies.head()
movies.describe()
Parentheses allows optional arguments
movies.describe(include='object')

Attributes: without parentheses

Description-oriented

movies.shape
movies.dtypes

Hit shift + tab multiple times to learn more about the parantheses

1x for a pop-up
2x for a larger pop-up
4x for a split-screen






