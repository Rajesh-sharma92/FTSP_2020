# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:50:00 2020

@author: Rajesh
"""

for num in range(0,51):
    if (num%3==0) and (num%5==0):
        print('FIZZBUZZ')
        
    elif num%3==0:
        print('FIZZ')
        
        

    elif num%5==0:
        print('BUZZ')
     
    else:
        print(num)
        
        
  
    print('*********************************')
    
    for i in range(0,26):
        if (i%3==0) and (i%5==0):
            print('fizzbuzz')
            
        elif i%3==0:
            print('fizz')
            
        elif i%5==0:
            print('buzz')
            
        else:
            print(i)
            
            