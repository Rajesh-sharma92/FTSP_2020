# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:51:55 2020

@author: Rajesh
"""

"""
Name: 
    Blackjack         
Filename:
    Blackjack.py
Problem Statement:
    Play a game that draws two random cards.
    The player then decides to draw or stick.
    If the score goes over 21 the player loses (goes ‘bust’).
    Keep drawing until the player sticks.
    After the player sticks draw two computer cards. 
    If the player beats the score they win. 
Data:
    Not required
Extension:
    Aces can be 1 or 11! The number used is whichever gets the highest score.  
""" 

import random

while(True):
        
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    
    list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    
    x = random.choice(list1)
    
    y = random.choice(list2)
    
    z = x+y 
    print('Player Score :', z)
    
    if z > 21 :
        print('goes ‘bust’')
        break
        
    else:
        
        a = random.choice(list1)
    
        b = random.choice(list2)
        
        c = a+b
        
        print('Computer Score :', c)
        
        if z > c :
            print('player WIN')
             
        else:
            
            print('Computer WIN')
            
            
            
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
    


