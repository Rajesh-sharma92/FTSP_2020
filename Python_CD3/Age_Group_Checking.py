# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:05:24 2020

@author: Rajesh
"""

# Take the age as input from the user and print whether he is a infant, Child , 
# Adult,  Senior Citizen
# 0 - 1 is Infant
# > 1 and < than 18 is Child 
# > 18 and < 60 is Adult
# > 60 is Senior Citizen 

while(True):
    
    age=int(input('Enter any Age to check the Age Group :'))
    
    if age>0 and age<=1:
        print('Infant')
    elif age>1 and age<=18:
        print('Child')
    elif age>18 and age<=60:
        print('Adult')
    elif age>60:
        print('Senior Citizen')
    
    

