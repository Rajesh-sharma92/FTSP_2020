# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 07:45:09 2020

@author: Rajesh
"""

n=int(input("Enter the number :"))
result=1
for i in range(n,0,-1):
    result=result*i
    
    print("The Factorial of",n,"is",result)
    
    
    