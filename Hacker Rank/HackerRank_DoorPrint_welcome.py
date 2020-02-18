# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:04:34 2020

@author: Rajesh
"""

x,y = input().split()
a = int(x)
b = int(y)
c = int((b-3)/2)
e = int((b-7)/2)
d = int(a/2)
if a%2 != 0 and b == a*3:
    for i in range(d):
        print('-'*(c-(3*i))+'.|.'*(2*i+1)+'-'*(c-(3*i)))
    print('-'*e+"WELCOME"+'-'*e)
    for i in range(d):
        print('-'*(3+(3*i))+'.|.'*(2*d-(2*i)-1)+'-'*(3+(3*i)))