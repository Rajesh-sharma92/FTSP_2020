# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 10:34:47 2020

@author: Rajesh
"""

"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""

s=input('Enter any string :')
up_Case=s.upper()
lo_Case=s.lower()
Camel_Title_Case=s.title() 
print('The Uperr case letters are :', up_Case)
print('The Lower case letters are :', lo_Case)
print('The Camel or Title case letters are :', Camel_Title_Case)
