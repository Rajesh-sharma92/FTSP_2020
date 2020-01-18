# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:56:11 2020

@author: Rajesh
"""
"""
# Take input string from the user, 
# print a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
"""


s=input('Enter any String :')
length=len(s)
if len(s)<=2:
    print('The Actual string :', s)
else:
    
    first_ltr=s[ : 2 : ]
    print('The First 2 Letters of String :', first_ltr)
    Last_ltr=s[-2 : : ]
    print('The Last 2 Letters of String :', Last_ltr)
    final_str=first_ltr+Last_ltr
    print('The Final string :', final_str)

