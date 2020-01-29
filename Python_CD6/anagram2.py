# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:04:03 2020

@author: Rajesh
"""

"""
Name: 
    Anagram 2        
Filename:
    anagram2.py
Problem Statement:
    Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
  
create a function which takes two arguments and return whether they are angram or no ( True or False)
Hint:
    Use dictionary to solve it 
"""

def add2nums(a,b): # finction define.
    
    return a+b

x=int(input('Enter the first number :'))

y=int(input('Enter the second number :'))

print(add2nums(x,y)) # function calling.

print(add2nums(190,10))

######### OR ############

def anagrams(a,b):
    
    return sorted(a)==sorted(b)
        
    
x=input('Enter the first string :')

y=input('Enter the second string :')

if anagrams(x,y):
    
    print('Both the strings are Anagrams : TRUE')
else:
    print('Both the strings are not Anagrams : FALSE')
    

















    
    
    
    




