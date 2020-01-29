# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:37:41 2020

@author: Rajesh
"""

"""
Name: 
    Pangram         
Filename:
    pangram.py
Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
Hint: 
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "the quick brown fox jumps over the lazy dog"  is a PANGRAM.  
Sample Input:
    The five boxing wizards jumps. 
    Sphinx of black quartz, judge my vow.
    The jay, pig, fox, zebra and my wolves quack!
    Pack my box with five dozen liquor jugs.
    
Sample Output:
    NOT PANGRAM 
    PANGRAM
    PANGRAM
    PANGRAM
"""  
s = input('Enter any string :')

def Pangram():
    
    str1 = 'abcdefghijklmnopqrstuvwxyz'

    for i in str1:
        
        if i in s:
            
            if i == str1[-1]:
                
                print('PANGRAM')
                
        else:
                
                print('NOT PANGRAM')
                
                break
Pangram()
                
#################### OR ###########################

str1 = 'abcdefghijklmnopqrstuvwxyz'
    
inp = input(">>")

inpp = inp.split()
    
d = "".join(inpp)
    
    
x = sorted(d)
z= set(x)
x = list(z)
x1 = sorted(x)
z = "".join(x1)
 
if z == str1:
    print("pangram")

else:
    print("not pangram")     
    
    
    
    
    
    
    
    