# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:50:42 2020

@author: Rajesh
"""

s=input('Enter some string :')
# s='MAMAJI' ' 'FUFAJI' 'RESTART'

s1 = s[0]
s2 = s[1 :]
s3 = (s1+s2.replace(s1,'$'))
print('The Replaced String :', s3)
    
    
