# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:33:06 2020

@author: Rajesh
"""

8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K.
   
   
import pandas as pd
df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

import matplotlib.pyplot as plt

plt.hist(df['salary'] , bins = range(50000 , 210000 , 15000) , color='Royalblue')

plt.axis([45000,210000,0,20])
plt.xlabel('No. of Salaries')
plt.ylabel('No.of Employees')
plt.title('Salaries Details')

plt.savefig('E:\Forsk Pandas\Hist_sal.jpg')
plt.show()


