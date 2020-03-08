# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 11:13:58 2020

@author: Rajesh
"""
"""
Code Challenge
  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Bahubali2_vs_Dangal.csv')
print(dataset)

  Days  Bahubali_2_Collections_Per_day  Dangal_collections_Per_day
0     1                           41.00                       29.78
1     2                           40.50                       34.82
2     3                           46.50                       42.35
3     4                           40.25                       25.48
4     5                           30.00                       23.07
5     6                           26.00                       21.20
6     7                           22.75                       20.29
7     8                           19.75                       17.00
8     9                           26.50                       31.27

features = dataset.iloc[:,: 1].values
labels = dataset.iloc[:,1].values

from sklearn.linear_model import LinearRegression
regg = LinearRegression()

regg.fit(features,labels)

a = regg.predict([[10]]) # Bahubali_2_Collections on 10 day.
a[0] # 17.416666666666668
------------------------------------------------------------------------------------------
features = dataset.iloc[:,: 1].values
labels = dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression
regg = LinearRegression()

regg.fit(features,labels)

b = regg.predict([[10]]) # Dangal_Collections on 10 day.
b[0] # 19.259444444444444
-------------------------------------------------------------------------------------------------------------

features = dataset.iloc[:,: 1].values
labels1 = dataset.iloc[:,1].values
labels2 = dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression
regg = LinearRegression()

regg.fit(features,labels1,labels2)

a = regg.predict([[10]])
a[0] # 18.934061808250192




























