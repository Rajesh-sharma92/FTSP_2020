# Handling missing values in pandas :- 

import pandas as pd

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)


df.head()
--------------
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00


df.tail()
------------
              City Colors Reported Shape Reported State              Time
18236   Grant Park             NaN       TRIANGLE    IL  12/31/2000 23:00
18237  Spirit Lake             NaN           DISK    IA  12/31/2000 23:00
18238  Eagle River             NaN            NaN    WI  12/31/2000 23:45
18239  Eagle River             RED          LIGHT    WI  12/31/2000 23:45
18240         Ybor             NaN           OVAL    FL  12/31/2000 23:59


         ''' NaN shows missing values '''
 

# checking which are NaN (True) using isnull
# creates DataFrame of True's and False's

df.isnull().tail()
----------------------
        City  Colors Reported  Shape Reported  State   Time
18236  False             True           False  False  False
18237  False             True           False  False  False
18238  False             True            True  False  False
18239  False            False           False  False  False
18240  False             True           False  False  False


df.notnull().tail()
--------------
       City  Colors Reported  Shape Reported  State  Time
18236  True            False            True   True  True
18237  True            False            True   True  True
18238  True            False           False   True  True
18239  True             True            True   True  True
18240  True            False            True   True  True


# count number of missing values in each column
# sum True's.

df.isnull().sum()
--------------------
City                  25
Colors Reported    15359
Shape Reported      2644
State                  0
Time                   0
dtype: int64

# we create a pandas series of booleans
booleans = pd.Series([True, False, True])

# use sum() on series
# this would sum all True
booleans.sum() # 2

# sum() uses axis=0 by default
# the following code does the same thing
# booleans.sum(axis=0)


# This allows us to see the 25 rows of missing values in the column City.

df[df['City'].isnull()]
# Here we will getting all 25 missing values.

df[df['City'].isnull()].head()
---------------------
    City Colors Reported Shape Reported State             Time
21   NaN             NaN            NaN    LA   8/15/1943 0:00
22   NaN             NaN          LIGHT    LA   8/15/1943 0:00
204  NaN             NaN           DISK    CA  7/15/1952 12:30
241  NaN            BLUE           DISK    MT   7/4/1953 14:00
613  NaN             NaN           DISK    NV   7/1/1960 12:00


 
'''  Q.1. What do we do about the missing values ? '''
 
        # Method 1: drop missing values.

df.shape  # (18241, 5)


# drop rows if any of the 5 columns have a missing value
# how='any' is the default, you need not include this

df.dropna().shape # (2486, 5)

df.dropna(how='any').shape # (2486, 5)

# no changes are made
# you can change using inplace='true'
# ufo.dropna(how='any', inplace=True).shape

df.dropna(how='any', inplace=True)

df.shape


# drop row if all of the columns are missing

df.dropna(how='all').shape  # (18241, 5)

# drop row if either City or Shape Reported are missing.

df.isnull().sum()
--------------------
City                  25
Colors Reported    15359
Shape Reported      2644
State                  0
Time                   0
dtype: int64


df.dropna(subset = ['City','Shape Reported'] , how = 'any').shape # (15576, 5)

# drop row if both City and Shape Reported are missing.

df.dropna(subset = ['City','Shape Reported'] , how = 'all').shape  # (18237, 5)



    #    Method 2: Filling missing values
    

# this shows missing values (NaN).

df['Shape Reported'].value_counts(dropna=False).head()
---------------------------
LIGHT       2803
NaN         2644
DISK        2122
TRIANGLE    1889
OTHER       1402
Name: Shape Reported, dtype: int64


# inplace=True makes the change to the data.

df['Shape Reported'].fillna(0).head()    
        
df['Shape Reported'].fillna(0).tail()       
18236    TRIANGLE
18237        DISK
18238           0
18239       LIGHT
18240        OVAL
Name: Shape Reported, dtype: object 


df['Shape Reported'].fillna(value = 'VARIOUS' , inplace = True)

df['Shape Reported'].tail(10)
---------------------------
18231        OVAL
18232     VARIOUS
18233     VARIOUS
18234    TRIANGLE
18235     VARIOUS
18236    TRIANGLE
18237        DISK
18238     VARIOUS
18239       LIGHT
18240        OVAL
Name: Shape Reported, dtype: object



df['Shape Reported'].value_counts(dropna=False).head()
------------------
VARIOUS     2977
LIGHT       2803
DISK        2122
TRIANGLE    1889
OTHER       1402
Name: Shape Reported, dtype: int64


df.columns

# We can do for any Columns like below steps :- 


df['City'].isnull().count() # 18241

df['City'].isnull().sum() # 25

df['City'].fillna(value = 'Python ML' , inplace = True)

df['City'].head()


df['City'].value_counts(dropna=False).head(30)


df['City'].str.contains('Python ML').head() # It is working fine.






