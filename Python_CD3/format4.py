# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:15:59 2020

@author: Rajesh
"""

"""
Problem Statement:
    This program accepts the user's first name and last name 
    Print them in reverse order with a space between them.
    Take Input from User 
    Your code should have only a single user input statement.  
"""


s=input('Enter any String to Print :')
l=s.split()
print('The Reversed string :', l[: : -1])
output=' '.join(l)
