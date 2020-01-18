# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:20:45 2020

@author: Rajesh
"""
"""

Problem Statement:
 Take first and last name in single command from the user and print  
 them in reverse order with a space between them, 
 find the index using find/index function and then print using slicing concept of the index.
 """
 
s=input('Enter your First Name & Last Name :')
l=s.split()
print('The Reversed string :', l[: : -1])


