# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:14:23 2020

@author: Rajesh
"""
from time import sleep
def fib_num(num):
    print('starting from .....')
    a,b = 0,1
    while(True):
        yield a
        a,b = b,a+b
        
fn = fib_num(100)

for item in fn:
    if item > 100:
        print('!!! Hey Man your work is done now !!!')
        break
    print(item)
    sleep(2)
