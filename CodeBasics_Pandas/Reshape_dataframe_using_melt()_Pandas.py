# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:11:49 2020

@author: Rajesh
"""

import pandas as pd

df = pd.read_csv('E:\CodeBasics_Pandas\Pandas_CSV_CB\weather4.csv')

df.head()
-------------
         day  chicago  chennai  berlin
0     Monday       32       75      41
1    Tuesday       30       77      43
2  Wednesday       28       75      45
3   Thursday       22       82      38
4     Friday       30       83      30

df1 = pd.melt(df,id_vars=['day'])
df1.head(10)
-----------------

         day variable  value
0     Monday  chicago     32
1    Tuesday  chicago     30
2  Wednesday  chicago     28
3   Thursday  chicago     22
4     Friday  chicago     30
5   Saturday  chicago     20
6     Sunday  chicago     25
7     Monday  chennai     75
8    Tuesday  chennai     77
9  Wednesday  chennai     75


df1[df1['variable']=='chicago']
---------
        day variable  value
0     Monday  chicago     32
1    Tuesday  chicago     30
2  Wednesday  chicago     28
3   Thursday  chicago     22
4     Friday  chicago     30
5   Saturday  chicago     20
6     Sunday  chicago     25

# Now we want to change the column Name like variable & Value.

df1 = pd.melt(df,id_vars=['day'],var_name='city',value_name='temperature')

df1.head()
----------------
         day     city  temperature
0     Monday  chicago           32
1    Tuesday  chicago           30
2  Wednesday  chicago           28
3   Thursday  chicago           22
4     Friday  chicago           30

-------------------------------------------------------------------------------------------------


# Create a simple dataframe 
  
# importing pandas as pd 
import pandas as pd 
  
# creating a dataframe 
df = pd.DataFrame({'Name': {0: 'John', 1: 'Bob', 2: 'Shiela'}, 
                   'Course': {0: 'Masters', 1: 'Graduate', 2: 'Graduate'}, 
                   'Age': {0: 27, 1: 23, 2: 21}}) 
print(df) 
------------
     Name    Course  Age
0    John   Masters   27
1     Bob  Graduate   23
2  Shiela  Graduate   21

# Name is id_vars and Course is value_vars 
pd.melt(df, id_vars =['Name'], value_vars =['Course']) 
--------------
    Name variable     value
0    John   Course   Masters
1     Bob   Course  Graduate
2  Shiela   Course  Graduate

pd.melt(df, id_vars =['Name'], value_vars =['Course','Age']) 
-------------
    Name variable     value
0    John   Course   Masters
1     Bob   Course  Graduate
2  Shiela   Course  Graduate
3    John      Age        27
4     Bob      Age        23
5  Shiela      Age        21

pd.melt(df, id_vars =['Name']) # value_vars is the default parameters.
------
    Name variable     value
0    John   Course   Masters
1     Bob   Course  Graduate
2  Shiela   Course  Graduate
3    John      Age        27
4     Bob      Age        23
5  Shiela      Age        21

df1 = pd.melt(df,id_vars=['Name'],var_name='New_Courese',value_name='New_Degree')
print(df1)
---------------
     Name New_Courese New_Degree
0    John      Course    Masters
1     Bob      Course   Graduate
2  Shiela      Course   Graduate
3    John         Age         27
4     Bob         Age         23
5  Shiela         Age         21





