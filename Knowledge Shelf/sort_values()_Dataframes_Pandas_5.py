# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:31:42 2020

@author: Rajesh
"""
"""
sort_values() in Dataframes Pandas :- 
-----------------------------------
"""
import pandas as pd

nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

# To check the Nan into the dataset we can check like this.
# It shows the all Nan values into dataset from top 5 from upper side & Last 5 from down side.
nba.head()

nba.tail()
nba.shape # (458, 9)

# It always shows Result into Ascending order only by default.
nba.sort_values('Name').head()

# If we want to display some of the details into Descending order then we need to change it to
# by = 'Ascending = True / False '. We will go for the False.

nba.sort_values('Name' , ascending = True).head() # By default it shows ascending order only.
nba.sort_values('Name' , ascending = False).head() # It shows the result into Descending order now.

nba.sort_values('Age').head() # By default it shows ascending order only.
nba.sort_values('Age' , ascending = False).head() # It shows the result into Descending order now.

# Here If we try to sort the salary values then all Nan values will come at the end.
nba.sort_values('Salary')

# Here All Nan values come at the first coz we have applied as tail() method. 
# By default na_position = 'last' always but we can change also.
nba.sort_values('Salary' , na_position = 'last').tail()

# Here All Nan values we can put at the first also.
nba.sort_values('Salary' , na_position = 'first').head()

---------------------------------------------------------------------------------------------------

"""
sort_values() for Multiple Columns in Pandas :-
----------------------------------------------
"""
import pandas as pd

nba = pd.read_csv(r'E:\Knowledge Shelf\csv Files\nba.csv')

# To check the Nan into the dataset we can check like this.
# It shows the all Nan values into dataset from top 5 from upper side & Last 5 from down side.
nba.head()

nba.tail()
nba.shape # (458, 9)

nba.sort_values(['Team','Name'])
# Default always ascending = True only but if you can we you want into Descending.
nba.sort_values(['Team','Name'] , ascending = True)
# Descending Order.
nba.sort_values(['Team','Name'] , ascending = False)

# Here we want to take the multiple columns like ascending & Descending order at a time.
# Here boolean values also we can pass into the list.
nba.sort_values(['Team','Name'] , ascending = [True,False])

# To make the changes into dataset always we need to call the Inplace = True then only it will work.
nba.sort_values(['Team','Name'] , ascending = [True,False] , inplace = True)
nba.head()



















