# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:15:54 2020

@author: Rajesh
"""

import math   # We need to import the math module.

dir(math)
 
num=int(input('Enter any number to convert into factorial :'))

fact=math.factorial(num)

print('The Factorial of :', fact)