# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:29:02 2020

@author: Rajesh
"""
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage.
   
import pandas as pd
df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

df[(df['sex'] == 'Female')].count()

df[(df['sex'] == 'Male')].count()

df['sex'].count()


df[(df['sex'] == 'Female')].count()

---------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

labels = 'Female','Male'
sizes = [39 , 39]
colors = ['green','skyblue']
explode = (0,0)

plt.pie(sizes , explode = explode , labels = labels , colors = colors , autopct = '%1.2f%%' , shadow = True , startangle = 270)
plt.axis('equal')

plt.savefig('E:\Forsk Pandas\Male_Female_Pie_Details.jpg')
plt.show








