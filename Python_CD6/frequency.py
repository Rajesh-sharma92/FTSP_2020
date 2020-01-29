# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:59:58 2020

@author: Rajesh
"""
"""
Name: 
    Character Frequency       
Filename:
    frequency.py 
Problem Statement:
    This program accepts a string from User and counts the number of characters 
    (character frequency) in the input string. 
Sample Input:
    www.google.com
Sample Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
""" 

from collections import Counter 

s = 'www.google.com'

output = Counter(s)

print('The occurences of each items are :', output)

 


 ######## OR ##############
  
import collections

s = input('Enter some the string :')

dict = {} # empty dictionary.

dict=collections.Counter(s)

print(dict)














    
    

    
    
    
    
    
    
    
    
    


