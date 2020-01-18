# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:12:03 2020

@author: Rajesh
"""

# Develop a program that will display a sentence backwards after entered.

s=input('Enter any string to print in Backwards :')
revstr=reversed(s)
print(type(revstr))
for ch in revstr:
    print(ch)
    


s=input('Enter any string :')
revstr=reversed(s)
output=''.join(revstr)
print(output)


s=input('Enter any string :')
l=s.split()
print('The entered details are :', l)
revstr=l[: : -1]
print('The Reversed String Details are :' , revstr)
output=' '.join(revstr)
print(output)

