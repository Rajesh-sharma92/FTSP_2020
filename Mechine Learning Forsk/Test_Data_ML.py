# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 07:39:27 2020

@author: Rajesh
"""

Question :- There are some values have given and pls find the solution for those 
values by using Linear Regresssion.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [1,2,3,4,5,6,7,8]

for what values of x = 15 and y = ?:

We know that, y = f(x)

straight Line = y = mx+c

where c = Intercept means where y-axis cuts.
and m = slope(Coefficent) = m = (y2-y1)/(x2-x1)
and where x, y co-ordinates are (x1,y1) , (x2,y2)

we can see that now straight line equation.

(5,4) , (5,4) ==> (x1,y1) , (x2,y2)

(y2-y1)/(x2-x1) 

(5-4)/(5-4) = 1.0

c = 0 and where x = 15
straight line equation.
y = mx+c
y = 1(15)+0

y = 15

y = f(x)

featues = [1,2,3,4,5,6,7,8]
labels = [1,2,3,4,5,6,7,8]

plt.scatter(featues,labels)
plt.plot(featues,labels,color='Pink')
plt.xlabel('features(Indepandent variables)')
plt.ylabel('labels(Depandent variables)')
plt.title('Simple Guessing Values for labels')
# plt.savefig('path')
plt.show()






















    
    