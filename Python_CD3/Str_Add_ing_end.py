# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:55:15 2020

@author: Rajesh
"""
"""
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Print the resulting string.

"""

s=input('Enter any string :')

if len(s)>=3:
      newstr=s+'ing'
      print('The New String :',newstr)
else:   
      s[-3 : ]=='ing'
      nwstr=s+'ly'
      print('The Newest String :', nwstr)
    
if len(s)<3:
      print('The String :', s)
            
            

    
