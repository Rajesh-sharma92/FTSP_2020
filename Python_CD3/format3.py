# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:32:02 2020

@author: Rajesh
"""

"""
Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    W*e*l*c*o*m*e* *t*o* *P*i*n*k* *C*i*t*y* *J*a*i*p*u*r

"""
s=input('Enter any string to print the output as per your choice :')
for ch in s:
    print(ch,end="*")


x=input('Enter any string to print the output :')
for letter in x:
    print(letter,end='-')
    
    