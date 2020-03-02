# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:27:42 2020

@author: Rajesh
"""

"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
 """  
   
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:\Forsk Pandas\CSV files\ign.csv')
print(df)

df.columns

df[(df['platform']=='Xbox 360') & (df['score']>7)]  # 909

------------------------------------------------------------------------------------
x = df[(df['platform']=='Xbox 360')]
y = df[(df['platform']=='PlayStation 4')]


plt.hist(x['score'],bins=[0,2,4,6,8,10])
plt.xlabel('Xbox 360')
plt.ylabel('score')

plt.hist(y['score'],bins=[0,2,4,6,8,10])
plt.xlabel('PlayStation 4')
plt.ylabel('score')

plt.savefig('E:\Forsk Pandas\CSV files\Ign.jpg')
plt.show()
















