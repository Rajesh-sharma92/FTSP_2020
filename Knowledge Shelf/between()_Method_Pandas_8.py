# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:26:33 2020

@author: Rajesh
"""
"""
between() Method in Pandas :-
---------------------------
"""
import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv' , parse_dates = ['Start Date','Last Login Time'])

df['Senior Management'] = df['Senior Management'].astype('bool') 
df['Gender'] = df['Gender'].astype('category')

df.head()

# Q1. To find the details of the employees like Salary Range , Commision & Joining Date at Company.

df[df['Salary'].between(90000,120000)]

df[df['Salary'].between(90000,120000)].shape # (263, 8)


df['Bonus %'].between(3,5)

df[df['Bonus %'].between(3,5)].shape # (115, 8)


df['Start Date'].between('1991-06-01' , '1992-12-01')

df[df['Start Date'].between('1991-06-01' , '1992-12-01')].shape # (47, 8)


df[df['Last Login Time'].between('08:30 AM' , '9:30 AM')].shape # (45, 8)


df[df['Last Login Time'].between('11:30 AM' , '2:30 PM')].shape # (138, 8)


df[df['Last Login Time'].between('14:00' , '15:30')].shape # (138, 8) # (65, 8)

--------------------------------------------------------------------------------------------------
"""
Duplicated() Method in Pandas :- 
-------------------------------
"""
import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv' , parse_dates = ['Start Date','Last Login Time'])

df['Senior Management'] = df['Senior Management'].astype('bool') 

df['Gender'] = df['Gender'].astype('category')

df.sort_values('First Name' , inplace = True)

df.head()

# How to check the duplicates values into dataset.

df['First Name'].duplicated()

df[df['First Name'].duplicated()].shape # (799, 8)

df[df['First Name'].duplicated()].head()

# It  will start searching from bottom to Top side when keep = 'last'
df['First Name'].duplicated(keep='last')

df[df['First Name'].duplicated(keep='last')].shape # (799, 8)


# It  will start searching from Top to bottom side when keep = 'first' and by default it is first only.
df['First Name'].duplicated(keep='first')

df[df['First Name'].duplicated(keep='first')].shape # (799, 8)


df['First Name'].duplicated(keep=False)

df[df['First Name'].duplicated(keep=False)].shape # (991, 8)


# How to find out the unique values into this dataset.{Dulicates should not be there}

# NOTE :- Here we have one special operator to get the unique values from dataset like (~) tield.
mask = ~ df['First Name'].duplicated(keep=False)

df[mask].shape # (9, 8)

----------------------------------------------------------------------------------------------------
"""
drop_duplicates() Method in Pandas :-
------------------------------------
"""
import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv' , parse_dates = ['Start Date','Last Login Time'])

df['Senior Management'] = df['Senior Management'].astype('bool') 

df['Gender'] = df['Gender'].astype('category')

df.sort_values('First Name' , inplace = True)

df.head()

# Here first we will check the length of the dataset by using python inbulit function len().
len(df) # 1000

len(df.drop_duplicates()) # 1000

df.drop_duplicates(subset=['First Name'] , keep = 'first')

len(df.drop_duplicates(subset=['First Name'] , keep = 'first')) # 201

df.drop_duplicates(subset=['First Name'] , keep = 'first').shape # (201, 8)


df.drop_duplicates(subset=['First Name'] , keep = 'first' , inplace = True)

# If there are such types of conditions then.
df.drop_duplicates(subset=['First Name','Team'] , keep = 'last' , inplace = True)


df.drop_duplicates(subset=['First Name','Team'] , inplace = True)



















