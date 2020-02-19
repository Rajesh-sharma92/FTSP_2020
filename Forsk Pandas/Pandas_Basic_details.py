# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:22:36 2020

@author: Rajesh
"""
# Panel data set = Pandas

''' Import python Library '''

import pandas as pd

''' create a Series from nd array '''

s = pd.Series(['a','b','c','d'])
print(type(s))
print(s)

NOTE :- Here we have not given any value for the index , by default it will be taking the Index.
Index always starts from zero(0) to len(data)-1, i.e., 0 to 3.
Ex :- 
s = pd.Series(['a','b','c','d','e','f','g'])
print(type(s)) # dtype: object in Pandas string means Objects.
print(s)

s = pd.Series([10,20,30,40,50])
print(s) # dtype: int64

NOTE :- By default Index always will be starting from 0 but if we want to give the index 
we can give from our end that is means Customized index.

s = pd.Series(['a','b','c','d','e','f','g'],index=[101,102,103,104,105,106,107]) # Customized index value.
print(s)
------------------------------------------------------------------------------------------
How to create Read the data from csv file :- 
-----------------------------------------
import pandas as pd

df = pd.read_csv('E:/PYTHON CODE Challenges/Pandas/Salaries.csv') # Reading a csv file into data frama.

# Not a good technique to print the Data Frame
print(df)
------------------------------------------------------------------------------------------------
# To check the data frames all data types & row and columns details.
df.info()
------------------------------------------------------------------------------------------
# To check no. of dimensions
df.ndim # 2 --> 2-Dimensional data
------------------------------------------------------------------------------------------
# Return a tuple representing the dimensionality.
df.shape # (78, 6) --- rows : 78 , Cols = 6
-------------------------------------------------------------------------------------------
# To check number of elements available in data frames.
df.size # 468 --> It gives the over all values available in the data Frame.
----------------------------------------------------------------------------------------------
# To get the List of first 5 records.
df.head(5) # It gives 5 records

df.head(10) # It gives 10 records

# Try to read the first 10, 20, 50 records.
df.head(10)
df.head(20)
df.head(50)
---------------------------------------------------------------------------------------------
# Can you guess how to view the last few records;
df.tail(5)

# Try to read the last 10, 20, 50 records.
df.tail(10)
df.tail(20)
df.tail(50)
---------------------------------------------------------------------------------------------
# Gives the row Indexes
df.index # RangeIndex(start=0, stop=78, step=1)
----------------------------------------------------------------------------------------
# list the column names / column Indexes.
df.columns 

O/P = Index(['rank', 'discipline', 'phd', 'service', 'sex', 'salary'], dtype='object')
----------------------------------------------------------------------------------------------
# To Check types for all the columns
df.dtypes
--------------------------------------------------------------------------------------------
# numpyrepresentation of the data
df.values 
--------------------------------------------------------------------------------------------
"""
Data Frames: method loc
If we need to select a range of rows, using their labels/index 
we can use method loc
"""
df.loc[:1] # It shows the output from o to 1 only coz it shows the last number details also.

df.loc[:5] # Last number means '5' will be inclusive into range.

df.loc[10:20,['rank','sex']]

df.loc[20:25,['sex','discipline']]
--------------------------------------------------------------------------------------------
"""
Data Frames: method iloc
If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""
df.iloc[:2] # 0 to 1. It shows the output from 0 to 1 only coz it wii not shows the last number details.

df.iloc[3:7] # 3 to 6.

df.iloc[ 10:21 , [0,4] ] # 0 = rank , 4 = sex
------------------------------------------------------------------------------------------------
# how to Select column rank and salary
df[['rank','salary']]

df[['phd','sex']]
------------------------------------------------------------------------------------------
# Find unique values in a Series / Column.
df['rank'] # It shows the full details of rank columan.

df['rank'].unique() # array(['Prof', 'AssocProf', 'AsstProf'], dtype=object)

df['discipline'].unique()

df['sex'].unique()

df['salary'].unique()

list1 = df['sex'].unique().tolist() # To convert into list.

print(list1) # ['Male', 'Female']
-------------------------------------------------------------------------------------------
# intuition about a Rank Series
df['rank']

df['rank'].value_counts()
           " OR "
df['rank'].value_counts(normalize = False)

********* O/P ************
   
Prof         46
AsstProf     19
AssocProf    13
Name: rank, dtype: int64
----------------------------------------------------------------------------   
df['sex'].value_counts()

********* O/P ************

Female    39
Male      39
Name: sex, dtype: int64
------------------------------------------------------------------------------------
# to show in Percentage 
df['rank'].value_counts(normalize = True)
            "OR"
df['rank'].value_counts(normalize = 1)
----------------------------------------------------------------------------------------
# To know the count of male and female candidates
df['sex'] 
df['sex'].value_counts()
df['sex'].value_counts(normalize = True)
-----------------------------------------------------------------------------------------
# count missing values 
# ( It also counts the NaN Values in the Series/Column)

df['sex'].value_counts(dropna=False)

df['phd'].value_counts()
df['phd'].value_counts(dropna=False)

df['salary'].value_counts()
df['salary'].value_counts(dropna=False)
-------------------------------------------------------------------------------------------
#calculate the basic statstics on the salary column

df['salary'].mean()
df['salary'].std()
df['salary'].describe()
df['sex'].describe()
----------------------------------------------------------------------------------------------
#Find how many values in the salary column which are non NaN (use count method);

df['salary'].count() # 76
df['phd'].count() # 76
df['sex'].count() # 78
--------------------------------------------------------------------------------------------
# Boolean Indexing
# Find those rows which has null values in salary/phd column

df['salary'].isnull() # 78

df[df['salary'].isnull()]

************  Output ************
        rank discipline   phd  service   sex  salary
7       Prof          A  18.0       18  Male     NaN
28  AsstProf          B   7.0        2  Male     NaN

df['phd'].isnull()

df[df['phd'].isnull()]

************  Output ************
         rank discipline  phd  service   sex    salary
13       Prof          B  NaN       33  Male  162200.0
34  AssocProf          B  NaN        8  Male  119800.0
-----------------------------------------------------------------------------------------------------
"""
Data Frames groupby method
Using "group by" method we can:
Split the data into groups based on some criteria
Calculate statistics (or apply a function) to each group
"""
# Group data using rank

df_rank= df.groupby(['rank'])

df_rank.size()
df_rank.count()
df_rank.groups

# Groups returns a dictionary object

df_rank.groups['AssocProf']
df_rank.groups['AssocProf'][0]
-------------------------------------------------------------------------------------------
# group data using rank followed  by discipline and sex

df_rank=df.groupby(['rank', 'discipline','sex'])
df_rank.groups
df_rank.count()
------------------------------------------------------------------------------------------
#Calculate mean value for each numeric column per each group
df_rank.mean()


 





















































































































































































































































































































































































