# Using "inplace" parameter in Pandas :- 

import pandas as pd

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)

df.shape  # (18241, 5)

df.head()
-----------------
                   City Colors Reported Shape Reported State             Time
0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00
3               Abilene             NaN           DISK    KS   6/1/1931 13:00
4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00


# dropping City column
df.drop('City', axis=1).head()
------------------
 Colors Reported Shape Reported State             Time
0             NaN       TRIANGLE    NY   6/1/1930 22:00
1             NaN          OTHER    NJ  6/30/1930 20:00
2             NaN           OVAL    CO  2/15/1931 14:00
3             NaN           DISK    KS   6/1/1931 13:00
4             NaN          LIGHT    NY  4/18/1933 19:00




# you can see that the City column is not gone 
# drop() method has inplace=False as default
df.shape # (18241, 5) 



# dropping City column
df.drop('City', axis=1 , inplace = True)


df.head()
------------
 Colors Reported Shape Reported State             Time
0             NaN       TRIANGLE    NY   6/1/1930 22:00
1             NaN          OTHER    NJ  6/30/1930 20:00
2             NaN           OVAL    CO  2/15/1931 14:00
3             NaN           DISK    KS   6/1/1931 13:00
4             NaN          LIGHT    NY  4/18/1933 19:00


df.shape # (18241, 4)


# dropna with how='any' would drop any row with 'NaN'

df.dropna(how='any').shape  # (2490, 4)


# as you can see, we lose a lot of rows because of dropna
# but the underlying data has not been affected because inplace=False for .dropna()

df.shape  # (18241, 4)


# some examples with inplace=False
# most are set to False

# ufo.set_index()
# ufo.rename()

# NOTE :- To make any changes we just need to use inplace = True.

# you can not use inplace=True and use an assignment instead
df = df.set_index('Time')

df.head()
---------------
                Colors Reported Shape Reported State
Time                                                
6/1/1930 22:00              NaN       TRIANGLE    NY
6/30/1930 20:00             NaN          OTHER    NJ
2/15/1931 14:00             NaN           OVAL    CO
6/1/1931 13:00              NaN           DISK    KS
4/18/1933 19:00             NaN          LIGHT    NY


df.fillna(method='bfill').tail()
------------------------
                Colors Reported Shape Reported State
Time                                                 
12/31/2000 23:00             RED       TRIANGLE    IL
12/31/2000 23:00             RED           DISK    IA
12/31/2000 23:45             RED          LIGHT    WI
12/31/2000 23:45             RED          LIGHT    WI
12/31/2000 23:59             NaN           OVAL    FL


df.fillna(method='ffill').tail()
------------------
                Colors Reported Shape Reported State
Time                                                 
12/31/2000 23:00             RED       TRIANGLE    IL
12/31/2000 23:00             RED           DISK    IA
12/31/2000 23:45             RED           DISK    WI
12/31/2000 23:45             RED          LIGHT    WI
12/31/2000 23:59             RED           OVAL    FL






