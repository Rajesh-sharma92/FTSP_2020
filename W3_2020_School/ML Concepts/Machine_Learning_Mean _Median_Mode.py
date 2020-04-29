# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:32:02 2020

@author: Rajesh
"""
'''
Machine Learning - Mean Median Mode :- 
------------------------------------------
'''
What can we learn from looking at a group of numbers ?

In Machine Learning (and in mathematics) there are often three values that interests us:

1) Mean - The average value
2) Median - The mid point value
3) Mode - The most common value

Ex :- We have registered the speed of 13 cars.

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

Q1. What is the average, the middle, or the most common speed value ?

1) Mean :- 
-----------
    
The mean value is the average value.

To calculate the mean, find the sum of all values, and divide the sum by the number of values:

(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

Ex :- Use the NumPy mean() method to find the average speed:

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x) # 89.76


2) Median :- 
---------------

The median value is the value in the middle, after you have sorted all the values:

77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111

It is important that the numbers are sorted before you can find the median.

The NumPy module has a method for this:

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x) # 87.0


NOTE :- If there are two numbers in the middle, divide the sum of those numbers by two.

    77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103

    (86 + 87) / 2 = 86.5

Ex :- 

import numpy

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x) # 86.5


3) Mode :- 
-------------
    
NOTE :- The Mode value is the value that appears the most number of times.


99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

The SciPy module has a method for this.

Ex :- 

Use the SciPy mode() method to find the number that appears the most:

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x) # ModeResult(mode=array([86]), count=array([3]))


NOTE :- Now we will take one more example.

Ex :- 

list1 = [10,20,30,40,50]

import numpy as np

x = np.mean(list1)

print('The Mean of List :', x)
------- Result ---------
The Mean of List : 30.0


------------------------------------------------------

Ex :- If we have 5 elements into the list.

list1 = [10,20,30,40,50]

import numpy as np

x = np.median(list1)

print('The Median of List :', x)
------- Result ---------
The Median of List : 30.0

Ex :- If we have 6 elements into the list.

list1 = [10,20,30,40,50,60]

import numpy as np

x = np.median(list1)

print('The Median of List :', x)
------- Result ---------
The Median of List : 35.0


------------------------------------------------------------------

Ex :- If we have 6 elements into the list.

list1 = [10,20,30,40,50,60,70,30,99,30,101,30]

from scipy import stats

x = stats.mode(list1)

print('The Mode of List :', x)
------- Result ---------
The Mode of List : ModeResult(mode=array([30]), count=array([4]))



Ex :- If we have 6 elements into the list.

list1 = [10,20,30,40,50,60,70,30,99,30,101,30,30,201,30]

from scipy import stats

x = stats.mode(list1)

print('The Mode of List :', x)
------- Result ---------
The Mode of List : ModeResult(mode=array([30]), count=array([6]))





