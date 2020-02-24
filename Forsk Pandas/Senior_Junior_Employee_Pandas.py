# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:45:06 2020

@author: Rajesh
"""
7. Who are the senior and junior most employees in the organization.

import pandas as pd
df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

df_rank = df.groupby('rank')[['service']].max()
print(df_rank)


********** Result **************
       service
rank              
AssocProf       24
AsstProf         6
Prof            51

df[(df['rank'] == 'AssocProf')]['service'].max() # 24

df[(df['rank'] == 'AsstProf')]['service'].max() # 6

df[(df['rank'] == 'Prof')]['service'].max() # 51


------------------------------------------------------------------------

df_rank = df.groupby('rank')[['service']].min()
print(df_rank)

********** Result **************
          service
rank              
AssocProf        6
AsstProf         0
Prof             0
-----------------------------------------------------------------------------------------

df[(df['rank'] == 'AssocProf')]['service'].min() # 6 

df[(df['rank'] == 'Prof')]['service'].min() # 0


df[(df['rank'] == 'AsstProf')]['service'].min() # 0










