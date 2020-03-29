# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:03:17 2020

@author: Rajesh
"""
"""
DataFrames in Pandas :-
---------------------
"""

import pandas as pd

nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

nba.head()

nba.tail()

nba.index # NOTE :- It is not a method and it is just a Object only.
# RangeIndex(start=0, stop=458, step=1)

nba.shape # (458, 9)

nba.ndim # 2

nba.size # 4122

nba.dtypes
********************
Name         object
Team         object
Number      float64
Position     object
Age         float64
Height       object
Weight      float64
College      object
Salary      float64
dtype: object

dataset.columns # This method is made for only DataFrames not series data.
******************
Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight',
       'College', 'Salary'],
      dtype='object')

dataset.axes
******************
[RangeIndex(start=0, stop=458, step=1),
 Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight',
        'College', 'Salary'],
       dtype='object')]


dataset.info # It provides the all information about the dataset.

# It counts all the data types seperately
dataset.get_dtype_counts()
*********************
float64    4
object     5
dtype: int64

---------------------------------------------------------------------------------------------------------------
"""
Shared Methods & Column Access in Pandas :- 
-----------------------------------------
"""

import pandas as pd

rev = pd.read_csv(r'E:\Knowledge Shelf\csv Files\revenue.csv')

rev.head()
*****************
  Date  New York  Los Angeles  Miami
0  1/1/16       985          122    499
1  1/2/16       738          788    534
2  1/3/16        14           20    933
3  1/4/16       730          904    885
4  1/5/16       114           71    253

rev = pd.read_csv(r'E:\Knowledge Shelf\csv Files\revenue.csv' , index_col='Date')
rev.head()
****************
        New York  Los Angeles  Miami
Date                                
1/1/16       985          122    499
1/2/16       738          788    534
1/3/16        14           20    933
1/4/16       730          904    885
1/5/16       114           71    253

rev.ndim # 2

# We have created the series and done the sum of the list elements and got the output.
s = pd.Series([1,2,3])
s.sum() # 6

# We have the dataset and we have got the sum of each columns like default always.
rev.sum()
**********************
New York       5475
Los Angeles    5134
Miami          5641

# If we want to get the sum of all rows present into a dataset.
rev.sum(axis=None)
*****************************
New York       5475
Los Angeles    5134
Miami          5641

rev.sum(axis=0) # If axis = 0 Means Column wise data.
New York       5475
Los Angeles    5134
Miami          5641

rev.sum(axis='index')
***********************************
New York       5475
Los Angeles    5134
Miami          5641


rev.sum(axis=1) # If axis = 1  Means Row wise data.
*************************
Date
1/1/16     1606
1/2/16     2060
1/3/16      967
1/4/16     2519
1/5/16      438
1/6/16     1935
1/7/16     1234
1/8/16     2313
1/9/16     2623
1/10/16     555

rev.sum(axis='columns')
************************************
Date
1/1/16     1606
1/2/16     2060
1/3/16      967
1/4/16     2519
1/5/16      438
1/6/16     1935
1/7/16     1234
1/8/16     2313
1/9/16     2623
1/10/16    555

nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

nba.head()

nba.Name.head()
---------------------------
0    Avery Bradley
1      Jae Crowder
2     John Holland
3      R.J. Hunter
4    Jonas Jerebko
Name: Name, dtype: object

nba.Name.dtypes # dtype('O')

# Checking data types of single column name like Name.
type(nba.Name) # pandas.core.series.Series

NOTE :- Here wa are able to extract the details of the single column but it is not recommaned
coz it may give any kind of error whenever we have any gap between the columnNames like.
Test_size --> OKay 
Test Size ---> It will not work properly. So, to overcome from this disadvantage we need to use 
like this to fetch the single columns details.

# This is good & Recommaned approach to fetcg the details.
nba['Name'].head()
*************************
0    Avery Bradley
1      Jae Crowder
2     John Holland
3      R.J. Hunter
4    Jonas Jerebko
Name: Name, dtype: object

nba['Team'].head()
*************************
0    Boston Celtics
1    Boston Celtics
2    Boston Celtics
3    Boston Celtics
4    Boston Celtics
Name: Team, dtype: object

nba[['Team','Name']].head()
*******************************
             Team           Name
0  Boston Celtics  Avery Bradley
1  Boston Celtics    Jae Crowder
2  Boston Celtics   John Holland
3  Boston Celtics    R.J. Hunter
4  Boston Celtics  Jonas Jerebko

nba[['Team','Name','Weight']].head()
*******************************************
             Team           Name  Weight
0  Boston Celtics  Avery Bradley   180.0
1  Boston Celtics    Jae Crowder   235.0
2  Boston Celtics   John Holland   205.0
3  Boston Celtics    R.J. Hunter   185.0
4  Boston Celtics  Jonas Jerebko   231.0

select = ['Team','Name','Weight'] # We can takes into a list all these columns.

nba[select].head()
************************
             Team           Name  Weight
0  Boston Celtics  Avery Bradley   180.0
1  Boston Celtics    Jae Crowder   235.0
2  Boston Celtics   John Holland   205.0
3  Boston Celtics    R.J. Hunter   185.0
4  Boston Celtics  Jonas Jerebko   231.0

---------------------------------------------------------------------------------------------------

"""
Add New Column to Dataframe in Pandas :-
-------------------------------------
"""
nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

nba.head()

# How to add new column into dataset.
nba['Sport'] = 'Basketball'

# To fetch the data from dataset.
nba['Sport'].head()
***********************
0    Basketball
1    Basketball
2    Basketball
3    Basketball
4    Basketball
Name: Sport, dtype: object

# To check whether new column is added or not.
nba.head()

nba['Leauge'] = 'National Basket Association'

# To fetch the data from dataset.
nba['Leauge'].head()
***********************
0    National Basket Association
1    National Basket Association
2    National Basket Association
3    National Basket Association
4    National Basket Association
Name: Leauge, dtype: object


# To check whether new column is added or not.
nba.head()

nba.insert(3,column='Games', value='Football')
nba.head()

nba.insert(0,column='Asian_Games' , value ='Football')
nba.head()

-------------------------------------------------------------------------------------------------
"""
Broadcasting Operations in Pandas :-
----------------------------------
"""
import pandas as pd

nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

nba.head()

nba['Salary'].sub(50000)
nba['Salary']- 50000

nba['Age'].head()
*************
0    25.0
1    25.0
2    27.0
3    22.0
4    29.0

nba['Age'].add(5).head()
****************
0    30.0
1    30.0
2    32.0
3    27.0
4    34.0

(nba['Age'] + 10).head()
**************************
0    35.0
1    35.0
2    37.0
3    32.0
4    39.0

nba['Weight'].mul(.500).head()
***********************
0     90.0
1    117.5
2    102.5
3     92.5
4    115.5

(nba['Weight']*.500).head()
***********************
0     90.0
1    117.5
2    102.5
3     92.5
4    115.5

# To New column into dataset and weight must be into kilograms.
nba['Weight In Kgs'] = nba['Weight'].mul(.500)
nba.head()
















