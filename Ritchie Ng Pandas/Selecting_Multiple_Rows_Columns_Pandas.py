# Selecting Multiple Rows and Columns :- 

1) loc
2) iloc
3) ix


import pandas as pd

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)

# show first 3 shows
df.head(3)
---------------
          City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke             NaN           OVAL    CO  2/15/1931 14:00


.loc usage
This is a really powerful and flexible method

# .loc DataFrame method
# filtering rows and selecting columns by label

# format
# df.loc[rows, columns]

# row 0, all columns
df.loc[0, :]
--------------
City                       Ithaca
Colors Reported               NaN
Shape Reported           TRIANGLE
State                          NY
Time               6/1/1930 22:00
Name: 0, dtype: object


df.loc[2, :]
--------------
City                       Holyoke
Colors Reported                NaN
Shape Reported                OVAL
State                           CO
Time               2/15/1931 14:00
Name: 2, dtype: object


# rows 0, 1, 2
# all columns

df.loc[[0, 1, 2], :]
--------------------
         City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke             NaN           OVAL    CO  2/15/1931 14:00

# more efficient code & Recommended to use this one only.
df.loc[0:2, :]
------------------
         City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke             NaN           OVAL    CO  2/15/1931 14:00


# if you leave off ", :" pandas would assume it's there
# but you should leave it there to improve code readability

df.loc[0:2]
----------------
          City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke             NaN           OVAL    CO  2/15/1931 14:00


# all rows
# column: City
df.loc[:, 'City'].head() 
------------------
0                  Ithaca
1             Willingboro
2                 Holyoke
3                 Abilene
4    New York Worlds Fair
Name: City, dtype: object


# all rows
# column: City, State
df.loc[:, ['City', 'State']]

# similar code for City through State
df.loc[:, 'City':'State']


# multiple rows and multiple columns
df.loc[0:2, 'City':'State']

# Multiple rows & multiple Columns
df.loc[2:4 , :]


# filter using City=='Oakland'
df[df['City'] == 'Oakland']


# again, specifying the rows and columns you want
# this would be the best way to do it compared to chain indexing 
df.loc[df['City'] == 'Oakland', 'State']



             ''' iloc usage '''


df.iloc[:, [0, 3]].head()
---------------
                   City State
0                Ithaca    NY
1           Willingboro    NJ
2               Holyoke    CO
3               Abilene    KS
4  New York Worlds Fair    NY


# iloc excludes 4 (compared to loc where it includes 4)
# iloc includes 0

df.iloc[:, 0:4].head()
------------------
                   City Colors Reported Shape Reported State
0                Ithaca             NaN       TRIANGLE    NY
1           Willingboro             NaN          OTHER    NJ
2               Holyoke             NaN           OVAL    CO
3               Abilene             NaN           DISK    KS
4  New York Worlds Fair             NaN          LIGHT    NY


# To get all Rows & All columns from DF.
df.iloc[: , :]


# To get all Rows & All columns from DF.
df.iloc[:]

# To get all Rows & All columns from DF.
df.iloc[: :]


df.iloc[,] # This is Invalid Syntax.


# this is the major difference
# exclusive of 3

df.iloc[0:3 , :]
----------------
          City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00
2      Holyoke             NaN           OVAL    CO  2/15/1931 14:00


# non-explicit code

df[['City', 'State']].head()
------------------
                   City State
0                Ithaca    NY
1           Willingboro    NJ
2               Holyoke    CO
3               Abilene    KS
4  New York Worlds Fair    NY


# explicit code
df.loc[:, ['City', 'State']].head()
---------------
                  City State
0                Ithaca    NY
1           Willingboro    NJ
2               Holyoke    CO
3               Abilene    KS
4  New York Worlds Fair    NY


df.loc[2:4 , ['City', 'State']].head()
------------------
                  City State
2               Holyoke    CO
3               Abilene    KS
4  New York Worlds Fair    NY


# ambiguous code again, are we referring to rows or columns?
df[0:2]
---------------
          City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00


# use iloc!
df.iloc[0:2, :]
------------------------
          City Colors Reported Shape Reported State             Time
0       Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00
1  Willingboro             NaN          OTHER    NJ  6/30/1930 20:00





