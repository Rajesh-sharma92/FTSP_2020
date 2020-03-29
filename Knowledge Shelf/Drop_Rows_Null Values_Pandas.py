# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:57:42 2020

@author: Rajesh
"""
"""
Drop Rows with Null Values in Pandas :-
------------------------------------
"""

import pandas as pd

nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

# To check the Nan into the dataset we can check like this.
# It shows the all Nan values into dataset from top 5 from upper side & Last 5 from down side.
nba.head()

nba.tail()
nba.shape # (458, 9)

# How to drop the all Nan values from Dataset at a time.
nba = nba.dropna()
nba.shape # (364, 9)

# By Default it will drop all the rows & cols values which are Nan into Dataset.
# We can use like this also and by default is the " how='any' ".
nba = nba.dropna(how='any') # (364, 9)

# If there all values are Nan into Dataset like in the any of the rows and some the values are 
# availble then it will not work it like " how='all' ".

# Here we can see that into dataset that row is having all values are Nan so easily we can 
# drop it by using the concept like " how = 'all' "
nba = nba.dropna(how='all')
nba.shape # (457, 9)

# Here inplace = True Means it will the performed operation into dataset also.
nba.dropna(how='all' , inplace=True) 

# Here We can check the Nan values into dataset and we can drop like Rows & Columns.
# By default " axis = 0 " --> Row and Cols --> " axis = 1"

nba.dropna(axis=0 , inplace=True)
nba.shape # (364, 9)

nba.dropna(axis=1 , inplace=False)
nba.shape # (458, 9)
nba 

nba.dropna(subset=['Salary'] , inplace = True)
nba.shape # (446, 9)
--------------------------------------------------------------------------------------------------------
"""
fillna() Method for Null Values in Pandas :-
-----------------------------------------
"""
import pandas as pd

nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

# To check the Nan into the dataset we can check like this.
# It shows the all Nan values into dataset from top 5 from upper side & Last 5 from down side.
nba.head()
nba.tail()

# To fill all the Nan Values with some of the values like.
# If we will means it will all the values like Number and Strings also. so we need to take it 
# sepeartely and then we should fill it.
nba.fillna(0 , inplace=True)
nba.head()

# To Check it whether changes happened or not.
nba['Salary'].fillna(0, inplace = True)
nba.head()

# To fill the string(objects) values into dataset like this.
nba['College'].fillna('FORSK' , inplace = True)
nba.head()























