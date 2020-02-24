# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:32:52 2020

@author: Rajesh
"""

3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same.
   
import pandas as pd
df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

df[df['salary'].isnull()]
mis_sal = df[df['salary'].isnull()]['service']
print(mis_sal)

df[(df['service']==18) | (df['service']==2)]

df1 = df[df['service']==18]
x = df1['salary'].mean()

df2 = df[df['service']==2]
y = df2['salary'].mean()

df[df['service']==18]['salary'].fillna(x)

4     104800.0
7     119190.0
33    120000.0
39    129000.0
49    122960.0

df[df['service']==18]['salary'].fillna(y)

4     104800.000000
7      76908.333333
33    120000.000000
39    129000.000000
49    122960.000000

