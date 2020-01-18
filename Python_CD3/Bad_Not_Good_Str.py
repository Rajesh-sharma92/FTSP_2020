# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:46:31 2020

@author: Rajesh
"""
"""
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

"""

s=input('Enter any string :')
a=s.index('not')
b=s.index('bad')+2
k=s.replace(s[a:b+1],'good')
print(k)




s=input('Enter any string :')
a=s.find('not')
b=s.find('bad')+2
k=s.replace(s[a:b+1],'good')
print(k)
