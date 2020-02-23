# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:29:46 2020

@author: Rajesh
"""


1. Which Male and Female Professor has the highest and the lowest salaries.

import pandas as pd
df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

df[(df['rank'] == 'Prof') & (df['sex'] == 'Male')]['salary'].max()
df[(df['rank'] == 'Prof') & (df['sex'] == 'Male')]['salary'].min()
df[(df['rank'] == 'Prof') & (df['sex'] == 'Female')]['salary'].max()
df[(df['rank'] == 'Prof') & (df['sex'] == 'Female')]['salary'].min()

-----------------------------------------------------------------------------------------------------

import pandas as pd
df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

2. Which Professor takes the highest and lowest salaries.

df[(df['rank'] == 'Prof')]['salary'].max()
df[(df['rank'] == 'Prof')]['salary'].min()

df[(df['rank'] == 'AssocProf')]['salary'].max()
df[(df['rank'] == 'AsstProf')]['salary'].max()


























