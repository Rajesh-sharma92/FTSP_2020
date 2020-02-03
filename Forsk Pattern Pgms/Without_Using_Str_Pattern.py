# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:24:40 2020

@author: Rajesh
""" 
" WAP to print this below pattern without using str function and by single print statement.

                    1
                    22
                    333
                    4444
                    55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='' if j < i else '\n')
        
        
        