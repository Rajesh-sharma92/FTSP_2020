# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:41:04 2020

@author: Rajesh
"""

"""
Name: 
    Reverse Function         
Filename:
    reverse.py
Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User
Sample Input:
    I am testing
Sample Output:
    gnitset ma I
    
""" 

def reverse(x):
    return x[: : -1]

x = input('Enter the string from user :')

print('The Reverse string :', reverse(x)) 



################ OR #################

def rev_string(str1):
    return str1[: : -1]

str1 = input('Enter the string from user :')

print('The Reverse string :', rev_string(str1)) 

################ OR #################

def rev_num(num):
    return num[: : -1]

num = input('Enter any number to reverse :')

print('The Reversed number :', rev_num(num))







