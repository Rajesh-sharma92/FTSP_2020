# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 07:43:01 2020

@author: Rajesh
"""

s = 'RAJESH'
list1 = s.split()
print(list1)

#####################
list1=[]
s = 'RAJESH'
for i in s:
    list1.append(i)
    print(list1)
##########################
s = 'RAJESH KUMAR SHARMA'
cnt = s.count('R')
print(cnt)

#########################

s = 'RAJESH KUMAR SHARMA'
low = s.lower()
print(low)

#####################

s = 'rajesh sharma from forsk'
upp = s.upper()
print(upp)

######################
s='RAJESH'
l=[]
j=0
k=2
for i in range(int(len(s)/2)):
    a=s[j:k]
    l.append(a)
    j+=2
    k+=2
print(l)

###########################
s='rAJEsH shArmA'

capital_letter = s.capitalize()

print(capital_letter)

############################

s='rAJEsH shArmA'

s.casefold()

#####################################

s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
j=0
k=n
for i in range(int(len(s)/2)):
    a=s[j:k]
    j+=n
    k+=n
print(l)






