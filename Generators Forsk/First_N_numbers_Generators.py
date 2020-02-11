# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:44:07 2020

@author: Rajesh
"""
" WAP to generate first N numbers by using generators concept."

from time import sleep
def firstN(num):
    print('starting from ......')
    n = 1
    while n < num:
        yield n
        n = n + 1
        if n == 11:
            print('!!! Your Work is DONE Now !!!')
        
fn = firstN(11)

for item in fn:
    print(item)
    sleep(1)
        

        


