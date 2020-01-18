# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:27:37 2020

@author: Rajesh
"""


from random import randint
print(randint(0,9))

# Generate floating random numbers from interval [3,7)

print(randint(3,7))

# O/P : 4

# Simulate the dice, random number between 1 and 6

print(randint(1,6))

# O/P : 3

# Random element from a list of rock, paper and scissors

import random
list=['rock','paper','scissors']
print(random.choice(list))

# O/P : Paper

import random
list=[]
list.append('Rock')
list.append('Paper')
list.append('Scissors')
print(random.choice(list))

# O/P : Rock