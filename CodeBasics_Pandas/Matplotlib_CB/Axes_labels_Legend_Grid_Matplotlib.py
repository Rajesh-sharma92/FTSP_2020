# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:25:58 2020

@author: Rajesh
"""
'''
Axes labels, Legend, Grid :- 
---------------------------
'''
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

max_t = [45,56,50,35,47,35,40]

min_t = [25,30,40,42,48,50,52]

avg_t = [10,25,15,22,31,45,44]

plt.plot(days,max_t)
plt.plot(days,min_t)
plt.plot(days,avg_t)
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Weather')
plt.legend()
plt.show()

# For the legend we just need to set the labels values to the particular rows.

plt.plot(days,max_t ,label='Max')
plt.plot(days,min_t , label='Min')
plt.plot(days,avg_t , label='Average')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Weather')
plt.legend()
#plt.show()

# If we want to set the Legend location then we can use the legend function.

# plt.legend(loc='upper right')

# plt.legend(loc='best') # loc= 'Best' is the default.

plt.legend(loc='Best' , shadow=True , fontsize='small')

plt.grid()

