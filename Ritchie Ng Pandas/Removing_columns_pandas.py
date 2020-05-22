# Removing columns from a pandas DataFrame :- 

import pandas as pd

# Creating pandas DataFrame

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)

df.head()

df.columns
--------------
Index(['City', 'Colors Reported', 'Shape Reported', 'State', 
       'Time'], dtype='object')


# To check the Shape of DataFrame.
df.shape # (18241, 5)

# NOTES :- 
# Removing column
# axis=0 row axis
# axis=1 column axis
# inplace=True to effect change

df.drop('Colors Reported' , axis = 1 , inplace = True)

df.shape # (18241, 4)

df.columns
----------
Index(['City', 'Shape Reported', 'State', 'Time'], dtype='object')


# How to Remove Multiple Columns from DF.

list_drop = ['City' , 'State' , 'Time']

df.drop(list_drop , axis = 1 , inplace = True)

df.columns
------------
Index(['Shape Reported'], dtype='object')

df.head()
-----------
  Shape Reported
0       TRIANGLE
1          OTHER
2           OVAL
3           DISK
4          LIGHT


df.drop('Shape Reported' , axis = 1 , inplace = True)

df.head()
-------------
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]


df.columns
--------------
Index([], dtype='object')



'''   How to Remove the Rows from DataFrames    '''


import pandas as pd

# Creating pandas DataFrame

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)

df.head()


# Removing rows 0 and 1
# axis=0 is the default, so technically, you can leave this out.

rows = 0

df.drop(rows , axis = 0 , inplace = True)

df.head()


rows = [1,2,3,4,5]

df.drop(rows , axis = 0 , inplace = True)

df.head()


rows = range(6,20)

df.drop(rows , axis = 0 , inplace = True)
 
df.head()


df

rows = range(0,18240)

df.drop(rows , axis = 0 , inplace = True)
 
df.head()
------------
       City Colors Reported Shape Reported State              Time
18240  Ybor             NaN           OVAL    FL  12/31/2000 23:59



rows = 18240

df.drop(rows , axis = 0 , inplace = True)
 
df.head()

Empty DataFrame
Columns: [City, Colors Reported, Shape Reported, State, Time]
Index: []








