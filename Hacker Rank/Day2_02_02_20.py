# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 12:04:24 2020

@author: Rajesh
"""

n = int(input())

d ={}

for i in range(n):
    
   name,*marks = input().split()
   
   scores = list(map(float, marks))
   
   Average = scores[0]+scores[1]+scores[2]/3
   
   print(round(Average,2))
   
   
   