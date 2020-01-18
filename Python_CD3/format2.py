# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:02:20 2020

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
    Welcome*to*Pink*City*Jaipur
 """
 
 s=input('Enter any string to print the output as per your choice :')
 l=s.split()
 output='*'.join(l)
 print(output)
 
 