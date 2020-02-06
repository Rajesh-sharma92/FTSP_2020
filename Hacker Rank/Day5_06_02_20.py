# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:38:25 2020

@author: Rajesh
"""

inp = input()
a = 0
b = 0
c = 0
d = 0
e = 0
for i in inp:
    if i.isalnum():
        a = 1
if a == 1:
    print("True")
else:
    print('False')
for i in inp:
    if i.isalpha():
        b = 1
if b == 1:
    print("True")
else:
    print('False')
for i in inp:
    if i.isdigit():
        c = 1
if c == 1:
    print("True")
else:
    print('False')
for i in inp:
    if i.islower():
        d = 1
if d == 1:
    print("True")
else:
    print('False')
for i in inp:
    if i.isupper():
        e = 1
if e == 1:
    print("True")
else:
    print('False')
    
