# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:15:08 2020

@author: Rajesh
"""

"""
Name: 
    Translate Function         
Filename:
    translate.py
Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User
Sample Input:
    This is fun
Sample Output:
    ToThohisos isos fofunon
""" 

str2=''

str1 = input('Enter some string :')

consonent = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

for i in str1:
    
    if i in consonent:
        
        str2 = str2 + (i + 'o' + i)
    else:
        str2 = str2 + i
        
print(str2)
        

#####################################################################



str1 = '' # Empty String.

s = input('Enter some string :')

conso = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

for i in s:
    
    if i in conso:
        
        str1 = str1 + (i + 'o' +i)
    else:
        str1 = str1 + i
        
print(str1)
    
    
######################## FOR VOWELS #########################################

while(True):
    
    s = input('Enter some string :')
    
    if not s:
        break
    
    vowels ='aeiouAEIOU'
    
    str1 = ''
    
    for i in s:
        
        if i in vowels:
            
            str1 = str1 + (i + 'V' +i)
            
        else:
            
            str1 = str1 + i
            
    print(str1)






























        
        
    
    
    
