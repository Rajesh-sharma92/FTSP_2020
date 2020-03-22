# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:41:55 2020

@author: Rajesh
"""
# For Linear values.
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]

plt.scatter(x,y)
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple X & Y Axis')
#plt.savefig('path')
plt.show()

-------------------------------------------------------------------------------------------
# For Different values not like Linear values.
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [3,5,7,8,2,0]

plt.scatter(x,y)
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple X & Y Axis')
#plt.savefig('path')
plt.show()

-----------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0,2.0,0.01)
s = 1 + np.cos(2*np.pi*t)

plt.grid()
plt.plot(t,s,'--')
plt.plot(t,s,'*')
plt.plot(t,s,'g')

plt.xlabel('Time(t)')
plt.ylabel('Voltage(mv)')
plt.title('Cosine wave plot (cosh(x))')
plt.show()

----------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0,5.0)
x2 = np.linspace(0.0,2.0)

y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
y2 = np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
plt.plot(x1,y1,'o-')
plt.title('subplot-1')
plt.xlabel('x1')
plt.ylabel('Amplitute(y1)')

plt.subplot(2,1,2)
plt.plot(x1,y1,'.-')
plt.title('subplot-2')
plt.xlabel('x2')
plt.ylabel('Amplitute(y2)')
plt.show()

--------------------------------------------------------------------------------------------
"""
BAR PLOT :-
--------
"""
import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
y = [10,24,36,40,5]
tick_label = ['one','two','three','four','five']
plt.bar(x,y,tick_label=tick_label,width=0.7,color=['Green','Blue'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Graph')
plt.show()

---------------------------------------------------------------------------------------------------
"""
Histogram Plot :-
-----------------
"""
import matplotlib.pyplot as plt

ages = [10,20,35,55,75,85,90,95,25,30]

range = (0,100)
bins = 5

plt.hist(ages,bins,range,color='pink',histtype='bar',rwidth=0.7)
plt.xlabel('Ages')
plt.ylabel('Bins')
plt.title('histogram Graph')
plt.show()

-----------------------------------------------------------------------------------------------------
"""
Scatter Plot in Matplotlib :-
--------------------------
"""

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,7,9,10,15,13,11,20]

plt.scatter(x,y,label='stars',color='green',marker='*',s=200)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.legend() # If you calling the labels then always you need to call the legend() also.
plt.show()
----------------------------------------------------------------------------------------------
"""
Pie Chart in Matplotlib :-
------------------------
"""
import matplotlib.pyplot as plt

activities = ['eat','sleep','work','drink']
slices = [3,7,8,6]
color = ['r','g','m','b']

plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True,autopct='%1.2f%%',explode=(0.2,0,0,0))
plt.legend()
plt.show()

-------------------------------------------------------------------------------------------------
"""
Plot Merging in Matplotlib :- 
--------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.01)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label='Sin')
plt.plot(x,y2,label='Cos')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.title('Sine & Cosine Functions')
plt.show()

------------------------------------------------------------------------------------------------
"""
Plot Data from CSV & Text Files using Matplotlib :-
------------------------------------------------
"""
import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('E:/Knowledge Shelf/Matplot.txt','r') as csvfile:
with open('E:/Knowledge Shelf/Matplot.csv','r') as csvfile:    
    
    plots = csv.reader(csvfile)
    for col in plots:
        x.append(col[0])
        y.append([col[1]])
        
plt.plot(x,y,label='File',color='green')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('Test Graph')
plt.legend()
plt.show()

        




























































