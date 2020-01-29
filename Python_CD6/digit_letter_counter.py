# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 22:44:05 2020

@author: Rajesh
"""
"""
Name: 
    Digit Letter Counter      
Filename:
    digit_letter_counter.py
Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits 
    and letters. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Store the letters and Digits as keys in the dictionary  
Sample Input:
    Python 3.2
Sample Output:
    Letters 6 
    Digits 2
""" 

s='a4b3c2'
x=len(s)
count=0

for i in s:
   if i.isalpha():
       count=count+1
       
print('Total words are :', count) 
print('Total Number are :', x-count)

 ########### OR ##############
 
s=input('Enter some of the string :')
 
x=len(s)
 
count=0
 
for i in s:
     if i.isalpha():
         count+=1
         
print('Total words are :', count) 
print('Total Number are :', x-count)

 ########### OR ##############
 
s = input('Enter some string with numbers :')

x=len(s)

count=0

for i in s:
    
    if i.isnumeric():
        count+=1
        
print('Total words are :', x-count) 
print('Total Number are :', count)

        
    
        
 




         
         



    
    

    




