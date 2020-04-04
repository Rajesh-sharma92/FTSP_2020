# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:09:38 2020

@author: Rajesh
"""
"""
The apply() Methods in Pandas :- 
--------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

bond.head()

def add_millions(number):
    return str(number) + ' MILLIONS!'

bond['Box Office'] = bond['Box Office'].apply(add_millions)

bond.head()

bond['Budget'] = bond['Budget'].apply(add_millions)
bond.head()
----------------------------------------------------------------------------------
def add_millions(number):
    return str(number) + ' MILLIONS!'

columns = ['Box Office','Budget','Bond Actor Salary']

for col in columns:
    
    bond[col] = bond[col].apply(add_millions)

bond.head()


--------------------------------------------------------------------------------------------
"""
The apply() Method with Row Values in Pandas :- 
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

bond.head()

def good_movie(row):
    actor = row[1]
    budget = row[4]
    
    if actor == 'Pierce Brosnan':
        return 'The Best Movie Ever'
    elif actor == 'Roger Moore' and budget > 40:
        return 'Just Enjoyable Movie'
    else:
        return 'I have No Idea'
bond.apply(good_movie , axis = 'columns')    

bond.head(10)






















