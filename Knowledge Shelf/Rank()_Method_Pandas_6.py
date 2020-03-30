# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:56:35 2020

@author: Rajesh
"""
"""
Rank Method in Pandas :- 
---------------------
"""
import pandas as pd

nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

# To check the Nan into the dataset we can check like this.
# It shows the all Nan values into dataset from top 5 from upper side & Last 5 from down side.
nba.head()

nba.tail()
nba.shape # (458, 9)

# Here we will drop all those values which are Nan into Dataset.
nba.dropna(how = 'all' , inplace = True)
nba.shape # (457, 9)

# It will work as same as the below line only like Inplace = True
nba['Salary'] = nba['Salary'].fillna(0)

nba['Salary'].fillna(0 , inplace = True)

print(type(nba['Salary'])) # <class 'pandas.core.series.Series'>

# We want to convert salaries into Integer Type.
nba['Salary'] = nba['Salary'].fillna(0).astype(int)
nba['Salary']

nba['Salary'].rank(ascending = False).astype(int)

# Here astype(int) or astype('int') both will work it.
nba['Salary_Rank'] = nba['Salary'].rank(ascending = False).astype(int)

nba.sort_values(by='Salary' , ascending = False , inplace = True)

nba.head()
    
    Salary          Salary_Rank  
  25000000.0            1  
  22970500.0            2  
  22875000.0            3  
  22359364.0            4  
  22192730.0            5  

----------------------------------------------------------------------------------------------------------
"""
Filtering Dataframe in Pandas :- 
-----------------------------
"""
import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv')

df.head()

df.info() # It contains lots of information but some times it will be wrong information and Wasting of m/y.
*******************
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 8 columns):
First Name           933 non-null object
Gender               855 non-null object
Start Date           1000 non-null object
Last Login Time      1000 non-null object
Salary               1000 non-null int64
Bonus %              1000 non-null float64
Senior Management    933 non-null object
Team                 957 non-null object
dtypes: float64(1), int64(1), object(6)
memory usage: 62.6+ KB


df['Start Date'].head()
****************************
0     8/6/1993
1    3/31/1996
2    4/23/1993
3     3/4/2005
4    1/24/1998
Name: Start Date, dtype: object

pd.to_datetime(df['Start Date']).head()
****************************
0   1993-08-06
1   1996-03-31
2   1993-04-23
3   2005-03-04
4   1998-01-24
Name: Start Date, dtype: datetime64[ns]

df['Start Date'] = pd.to_datetime(df['Start Date'])

df['Last Login Time'].head() # This is not object coz it is numbers.
*********************************
0    12:42 PM
1     6:53 AM
2    11:17 AM
3     1:00 PM
4     4:47 PM
Name: Last Login Time, dtype: object

df['Last Login Time'] = pd.to_datetime(df['Last Login Time'])

df['Senior Management'].head() # This is not object coz it is Boolean values.
*********************************
0     True
1     True
2    False
3     True
4     True
Name: Senior Management, dtype: object

df['Senior Management'] = df['Senior Management'].astype(bool) # .astype('bool')

df['Senior Management'].head()
**********************************
0     True
1     True
2    False
3     True
4     True
Name: Senior Management, dtype: bool

df['Gender'].head()
**************************
0      Male
1      Male
2    Female
3      Male
4      Male
Name: Gender, dtype: object

df['Gender'] = df['Gender'].astype('category')

df['Gender'].head()
************************
0      Male
1      Male
2    Female
3      Male
4      Male
Name: Gender, dtype: category
Categories (2, object): [Female, Male]

df.info()
********************
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 8 columns):
First Name           933 non-null object
Gender               855 non-null category
Start Date           5 non-null datetime64[ns]
Last Login Time      1000 non-null datetime64[ns]
Salary               1000 non-null int64
Bonus %              1000 non-null float64
Senior Management    1000 non-null bool
Team                 957 non-null object
dtypes: bool(1), category(1), datetime64[ns](2), float64(1), int64(1), object(2)
memory usage: 49.0+ KB

NOTE :- We can see that the total difference b/w print(49.0/62.6) # 0.78
--------------------------------------------------------------------------------------------
NOTE :- All these above operations we can perform like this also.

import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv' , parse_dates = ['Start Date','Last Login Time'])

df['Senior Management'] = df['Senior Management'].astype('bool') 
df['Gender'] = df['Gender'].astype('category')

df.head()

df.info()
***************
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 8 columns):
First Name           933 non-null object
Gender               855 non-null category
Start Date           1000 non-null datetime64[ns]
Last Login Time      1000 non-null datetime64[ns]
Salary               1000 non-null int64
Bonus %              1000 non-null float64
Senior Management    1000 non-null bool
Team                 957 non-null object
dtypes: bool(1), category(1), datetime64[ns](2), float64(1), int64(1), object(2)
memory usage: 49.0+ KB

--------------------------------------------------------------------------------------------------------

"""
Filtering a Dataframe Based on a Condition :-
-----------------------------------------------
"""
import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv')

df['Gender'] == 'Male'

df[df['Gender'] == 'Male'].shape # (424, 8)

df['Team'] == 'Finance'

df[df['Team'] == 'Finance'].shape # (102, 8)

NOTE :- The above task you can also performed like this also.

mask = df['Team'] == 'Finance'
df[mask]
df[mask].head()

# Here in the senior Management we have already values are True & False condition.
df[df['Senior Management'] == True]

df[df['Senior Management'] == False]

NOTE :- To find the employees details those are not working into Marketing Team.

df['Team'] != 'Marketing'

df[df['Team']!= 'Marketing']

df[df['Team'] != 'Marketing'].shape # (902, 8)

df[df['Team'] != 'Marketing'].head()

df['Salary'] > 110000

df[df['Salary'] > 110000].shape # (322, 8)

df[df['Salary'] > 110000].head(10).count()

df[df['Salary'] > 110000].count()
***********************************************
First Name           295
Gender               282
Start Date           322
Last Login Time      322
Salary               322
Bonus %              322
Senior Management    295
Team                 306

df[df['Bonus %'] < 1.5].shape # (28, 8)

mask = df['Start Date'] < '1985-01-01'
df[mask].head()

df[mask].shape # (332, 8)























































