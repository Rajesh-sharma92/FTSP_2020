# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:41:49 2020

@author: Rajesh
"""
"""
Code Challenge
  Name: 
    Automobile Analysis
  Filename: 
    automobile.py
  Problem Statement:
    (Automobile.csv)
    Read the Automobile.csv file and perform the following task :
    1. Handle the missing values for Price column
    2. Get the values from Price column into a numpy.ndarray
    3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

import pandas as pd

df = pd.read_csv('E:\Forsk Pandas\CSV files\Automobile.csv')

a = df[df['price'].isnull()]
print(a)

for i in a['city_mpg']:
    df[df['city_mpg']==i] = df[df['city_mpg']==i].fillna(0)

df[df['price'].isnull()]

--------------------------------------------------------------------------------------------------------------
import pandas as pd

df = pd.read_csv('E:\Forsk Pandas\CSV files\Automobile.csv')

a = list(df['price'])

import numpy as np

arr = np.array(a)


-----------------------------------------------------------------------------------------------
df['price'].max()  # 45400.0
df['price'].min() # 0.0
df['price'].mean() # 12949.42
df['price'].std() # 8079.04





