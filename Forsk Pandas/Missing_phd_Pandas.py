# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:43:06 2020

@author: Rajesh
"""

4. Missing phd - should be mean of the matching service.

import pandas as pd
df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

mis_phd = df[df['phd'].isnull()]['service']

df[(df['service'] == 33) | (df['service'] == 8)]

df1 = df[df['service'] == 33]

x = df1['service'].mean()

df2 = df[df['service'] == 8]

y = df2['service'].mean()

df[df['service'] == 33]['phd'].fillna(x)

10    39.0
13    33.0

df[df['service'] == 8]['phd'].fillna(y)

34     8.0
37    20.0
41    13.0
56    10.0

