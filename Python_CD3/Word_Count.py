# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:05:24 2020

@author: Rajesh
"""


# Write a program to count the number of words in a sentence.

s = input('Enter any string :')
l = s.split(' ') # The string is splitted by space between sentence.
length = len(l)
print('The total number of words :' , length)


