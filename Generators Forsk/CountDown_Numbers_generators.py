# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:26:25 2020

@author: Rajesh
"""
from time import sleep
def countdown(num):
    print('countdown starting from .....')
    while num > 0:
        yield num
        num = num - 1
        if num == 0:
            print('!!! TASK COMPLETED !!!')
        
values = countdown(10)

print(type(values))

# print(next(values))
# sleep(1)

for item in values:
    print(item)
    sleep(1)
    
    