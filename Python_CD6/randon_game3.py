# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:02:00 2020

@author: Rajesh
"""
"""
Name: 
    Random Game 3         
Filename:
    randon_game3.py
Problem Statement:
    Write a program for a Higher / Lower guessing game
    The computer randomly generates a sequence of up to 10 numbers
    between 1 and 13. The player each after seeing each number
    in turn has to decide whether the next number is higher or lower.
    If you can remember Brucie’s ‘Play your cards right’ it’s basically
    that. If you get 10 guesses right you win the game.
    Starting number : 12
    Higher(H) or lower(L)? L
    Next number 8
    Higher(H) or lower(L)? L
    Next number 11
    You lose
Extension:
    Give the players two lives
    Make sure only H or L can
    be entered  
Hint: 
    Use a condition controlled loop (do until, while etc) to control the
    game. Do not find yourself repeating the same code over and over!
    You don't need to remember all 10 numbers just the current number
    /next number. Don’t forget you’ll have to keep a count of the
    number of turns they’ve had. 
""" 

import random

num1 = random.randint(1,14)

print('starting number :', num1)

for i in range(10):
    
    num2 = random.randint(1,14)
    list1 =[]
    list1.append(num2)
    print('Next Number :', list1)
    
    guess = input('Enter Highher(H) or Lower(L) ? ')
    
    if guess == 'H':
    
        if num2 > num1:
            
            print('You Won')
            
        else:
            
            print('You Lose')
            
            if guess == 'L':
            
                if num2 < num1:
                
                    print('You Won')
            
                else:
            
                    print('You Lose')
            
            
            
            
                
                
            
            
    
    









