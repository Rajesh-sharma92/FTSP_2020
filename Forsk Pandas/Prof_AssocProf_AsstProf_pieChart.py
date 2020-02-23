# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:45:57 2020

@author: Rajesh
"""

6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers and Graphically using a Pie Chart.
   
   
import pandas as pd
df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

df_Prof = df[(df['rank'] == 'Prof')]
df_Prof.count() # 46

df_Prof = df[(df['rank'] == 'AssocProf')]
df_Prof.count() # 13

df_Prof = df[(df['rank'] == 'AsstProf')]
df_Prof.count() # 19
   
--------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt  

labels = 'Prof' , 'AssocProf' , 'AsstProf'
sizes = [46,13,19]
colors = ['blue','Red','lightgreen']
explode = (0,0,0)

plt.pie(sizes, explode = explode , labels = labels , colors = colors , autopct = '%1.2f%%' , shadow = 'True' , startangle = 270 )
# plt.pie(sizes, explode = explode , labels = labels , colors = colors , autopct = '%1.3f%%' , shadow = 'False' , startangle = 90 )
plt.axis('equal')
plt.savefig('E:\Forsk Pandas\Prof_AssocProf_AsstProf.jpg')
plt.show()
 




