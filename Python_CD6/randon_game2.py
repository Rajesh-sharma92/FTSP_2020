# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:44:46 2020

@author: Rajesh
"""

"""
Name: 
    Random Game 2         
Filename:
    randon_game2.py
Problem Statement:
    Write a program for a game where the computer generates a
    random starting number between 20 and 30.
    The player and the computer can remove 1,2 or 3 from the number
    in turns. Something like this...
    Starting number : 25
    How many do you want to remove? 3
    22 left
    Computer removes 2
    20 left
    The player who has to remove the last value to bring the number
    down to 0 is the loser.
    1 left
    Computer removes 1
    You win!
    Easy option
    Get the computer to choose a number between 1—3 at random
    Harder option
""" 
import random

num = random.randint(20,30)

print('The Starting no :' , num)

while num > 0: 
    
    Player = int(input('How many no. do you want to remove :'))
    
    num = num - Player
    
    print('The Left :', num)
    
    if num == 0:
        
        print('YOU HAVE LOST THE GAME')
        
        break
    else:
        
        Computer = random.randint(1,4)
        
        num = num - Computer
        
        print('The Computer Removes :', num)
        
        if num == 0:
            
            print('YOU HAVE WON THE GAME')
            
            
            
        
    
    






























import random

num = random.randint(20,30)
print("Starting number :",num)

while num >0:
    
    user = int(input("how many do you want to remove: "))
    num = num-user
    print(num,"Left")
    if num == 0:
        print("You Lose")
        break
    else:
    
        comp = random.randint(1,3)
    print("computer removes:",comp)
    num = num - comp
    print(num, "Left")
    if num == 0:
        print("You Win!")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





























