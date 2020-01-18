# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:19:45 2020

@author: Rajesh
"""
"""
# Given a string s, print the string again
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: try using replace function
"""

s=input('Enter any string :')
a=s[0]
b=s[1 :].replace(a,'*')
k=a+b
print('The String :', k)


 # output :- ba**le
 
s=input('Enter any string :')
x=s[0]
b=s[1 :].replace(a,'%')
k=a+b
print('The String :', k)

  # output :- bum%%le