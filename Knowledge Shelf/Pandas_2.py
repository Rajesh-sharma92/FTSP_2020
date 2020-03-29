# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:20:16 2020

@author: Rajesh
"""
"""
value_counts Methods in Pandas :-
------------------------------
"""
import pandas as pd
dataset = pd.read_csv('E:/Knowledge Shelf/csv Files/Salary_Classification.csv')
dataset.ndim

dataset.head()
*********************
             WorkedHours  Certification  YearsExperience  Salary
Department                                                      
Development         2300              0              1.1   39343
Testing             2100              1              1.3   46205
Development         2104              2              1.5   37731
UX                  1200              1              2.0   43525
Testing             1254              2              2.2   39891

dataset['Department']

dataset['Department'].value_counts()
*****************************************
Development    10
UX             10
Testing        10

dataset.count()
*****************
Department         30
WorkedHours        30
Certification      30
YearsExperience    30
Salary             30
dtype: int64

dataset['Department'].count() # 30

dataset['Department'].value_counts().sum() # 30


dataset['Certification'].value_counts()
******************************
2    9
3    8
1    8
4    3
0    2
Name: Certification, dtype: int64

dataset['Certification'].count()  # 30

dataset['Salary'].value_counts(ascending=True)

dataset['Department'].value_counts(ascending=True)
************************
Testing        10
UX             10
Development    10

Name: Department, dtype: int64

--------------------------------------------------------------------------------------------------
"""
apply() Methods in Pandas :- 
-------------------------
"""
import pandas as pd
dataset = pd.read_csv('E:/Knowledge Shelf/csv Files/Salary_Classification.csv')
dataset = dataset.drop('Department', axis=1) # Department col is not available into dataset.


dataset.columns
************************
['WorkedHours', 'Certification', 'YearsExperience','Salary']


ds1 = dataset['Salary']

def classify_per(n):
    if n < 40000 :
        return 'OKAY'
    elif n >= 50000 and n < 120000:
        return 'Satisfactory'
    else:
        return 'Incrediable'
    
ds1 = ds1.apply(classify_per)    
print(ds1)

ds1.count() # 30

ds1.apply(lambda n : n*2)






















