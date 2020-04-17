# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:29:00 2020

@author: Rajesh
"""
'''
Matplotlib Introduction :- 
-------------------------
'''
import matplotlib.pyplot as plt

# %matplotlib inline # Just used into Jupyter Notebook.

x = [1,2,3,4,5,6,7]

y = [50,51,85,65,56,45,35]

plt.plot(x,y , color='Blue' , linewidth=5 , linestyle='dashed')

plt.plot(x,y , color='Red' , linewidth=2 , linestyle='dashdot')

plt.plot(x,y , color='Green' , linewidth=5 , linestyle='dotted')

plt.xlabel('No. Of Days')
plt.ylabel('Temperature')
plt.title('Days & Temperature Graph')
plt.show()

------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

# %matplotlib inline # Just used into Jupyter Notebook.

x = [1,2,3,4,5,6,7]

y = [50,51,85,65,56,45,35]

plt.plot(x,y , 'g+')

plt.plot(x,y , 'g+--')

plt.plot(x,y , 'g+-.')

plt.plot(x,y , '--r')

plt.plot(x,y , 'gD')

# Here we can specify the values from our end also.

plt.plot(x,y, color='Blue',marker='D' ,linestyle='')


plt.plot(x,y, color='Red',marker='+' ,linestyle='' , markersize=20)

# If we want to make it visiable or not the plotted line.
# We just need to set the value of alpha parameters.

plt.plot(x,y, color='Red' , alpha = 1)

plt.plot(x,y, color='Red' , alpha = 0)

plt.plot(x,y, color='Red' , alpha = 0.5)

plt.plot(x,y, color='Red' , alpha = 0.1)

