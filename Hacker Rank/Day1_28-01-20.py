# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:25:36 2020

@author: Rajesh
"""
""" 

Pg (1) :- 

num = int(input())
if num%2==0:
     
    if num>=2 and num<=5:
        print('Not Weird')
        
    elif num>=6 and num<=20:
        print('Weird')
        
    elif num > 20:
        print('Not Weird')
else:
    
    print('Weird')
    
    
    
Pg (2) :-   

    
a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)



Pg (3) :- 

a = int(input())
b = int(input())

print(a//b)
print(a/b)



Pg (4) :- 

num = int(input())
for i in range(num):
    square = i*i
    print(square)
  
    
Pg (5) :- 

def is_leap(num):
    
    
    # Write your logic here
    
    if num%400==0:
        return True
    
    elif num%100==0:
        return False
        
        
    elif num%4==0:
         return True
    
    else:
        return False

year = int(input())
print(is_leap(year))



"""










        