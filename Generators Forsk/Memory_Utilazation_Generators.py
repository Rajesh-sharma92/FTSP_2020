# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 07:56:39 2020

@author: Rajesh
"""
import time
import random

names = ['sunny','bunny','chiiny','vinny']
subjects = ['python','java','blockchain']

def people_list(num): # for list.
    results = []
    for i in range(num):
        person = {
                'id':i,
                'name':random.choice(names),
                'subject':random.choice(subjects)
                }
        results.append(person)
        return results
    
def people_generator(num): # for generators.

    for i in range(num):
        person = {
            'id':i,
            'name':random.choice(names),
            'subject':random.choice(subjects)
            }
    yield person
    
t1 = time.perf_counter()
people = people_generator(100000)
t2 = time.perf_counter()
print('Time Taken for Generators :',t2-t1)

t1 = time.perf_counter()
people = people_list(100000)
t2 = time.perf_counter()
print('Time Taken for list :',t2-t1)

