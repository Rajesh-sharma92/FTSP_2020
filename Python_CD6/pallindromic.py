# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:13:51 2020

@author: Rajesh
"""
"""
Name: 
    Pallindromic Integer
Filename: 
    pallindromic.py
Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)        
Data:
    Not required
Extension:
    Not Available  
Hint: 
    A palindromic number or numeral palindrome is a number that remains the same
    when its digits are reversed. 
    Like 16461, for example, it is "symmetrical"  
"""
while(True):
    
    num=input('Enter any number :')
        
    a=num[:]
    
    rev_a=num[: : -1]
    
    if not num:
        break
    
    if a==rev_a:
        
        print('True')
        
    else:
        
        print('False')
        
    