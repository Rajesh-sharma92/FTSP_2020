# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:48:30 2020

@author: Rajesh
"""
"""
Filename:
    code_breaker.py
Problem Statement:
    The computer generates a 4 digit code
    The user types in a 4 digit code. Their guess.
    The computer tells them how many digits they guessed correctly
Data:
    Not required
Extension:
    the computer tells them how many digits are guessed correctly 
    in the correct place and how many digits have
    been guessed correctly but in the wrong place.
    The user gets 12 guesses to either 
    WIN – guess the right code. 
    Or
    LOSE – run out of guesses.  
"""
 
#digit=input('Enter some 4 digits numbers : ')

from random import randint

d1=print(randint(0,9) , randint(0,9) , randint(0,9) , randint(0,9))

digit=input('Enter some 4 digits numbers : ')

if digit == d1:
    
    print('WIN – guess the right code.')
else:
    print('LOSE – run out of guesses.')
    

################ OR ################## 
    
from random import randint

digit1=[randint(0,9) , randint(0,9) , randint(0,9) , randint(0,9)]

print('The Random Numbers are :' , digit1)

d1=[int(input('Enter first digit :')),int(input('Enter second digit :')),int(input('Enter third digit :')),int(input('Enter fourth digit :'))]

if digit1[0] == d1[0]:
    print('First digit guessed correctly')

if digit1[1] == d1[1]:
    print('second  digit guessed correctly')

if digit1[2] == d1[2]:
    print('Third digit guessed correctly')

if digit1[3] == d1[3]:
    print('Fourth digit guessed correctly')
    
    if digit1 == d1:
        print('WIN – guess the right code.')
    else:
        print('LOSE – run out of guesses.')




















    
    
    
