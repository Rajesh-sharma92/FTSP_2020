# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:02:11 2020

@author: Rajesh
"""
"""
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.

"""
a=input('Enter first string :')
b=input('Enter second string :')

a1=a[0:2]
b1=b[0:2]
a2=a[2:]
b2=b[2:]

print(b1+a2 , a1+b2)

