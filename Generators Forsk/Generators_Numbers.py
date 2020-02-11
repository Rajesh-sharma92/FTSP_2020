# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:15:50 2020

@author: Rajesh
"""

'''Difference between a regular function and generator function '''
# Regular Function.
def function_a():
    # a lots of code lines.
    return 'a'

function_a() # Function call. O/P = a
------------------------------------------------
# Generators function.
def generators_a():
    yield 'a'
    
generators_a() # < generator object generators_a at 0x000000000907CD48 >
-------------------------------------------------------------

def city_generator():
    yield('Bangalore')
    yield('jaipur')
    yield('sikar')
    yield('salasar')
    yield('Ajmer')
    
city = city_generator()
print(type(city))

print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))


city = city_generator()
# Start again generating values.

#Generators are iterables themselves. 
for item in city:
    print(item)
    
----------------------------------------------------------------
def brand_generator():
    yield('Puma')
    yield('Reebok')
    yield('Louis philips')
    yield('zara')
    
brand = brand_generator()
print(type(brand))

print(next(brand))
print(next(brand))
print(next(brand))
print(next(brand))

# Start again generating values.
brand = brand_generator()
#Generators are iterables themselves. 
for item in brand:
    print(item)
--------------------------------------------------------------------

"""  Example of Counting  """    
def countdown(num): # Generator here is "countdown()"
    print('Starting from here')
    while num > 0:
        yield num
        num = num - 1
    
mycountdown =  countdown(10)
print(type(mycountdown))

print(next(mycountdown))
 
------------------------------------------------------------------   
"""  Example of Counting  """     
def countdown(num):
    print('starting the numbers from here')
    while num > 0:
        yield num
        num = num + 1
        if num == 25:
            print('STOP ITERATING ME GUYS NOW')
            break
       # num += 1
mycountdown = countdown(20)
print(type(mycountdown))

print(next(mycountdown))

-----------------------------------------------------------------
def even_num(num):
    print('The Even numbers are starting from :')
    while num > 0:
        yield num
        num = num - 1
        if num%2==0:
            print('Even numbers are :')
        else:
            print('Odd Numbers are :')
myeven = even_num(10)
print(type(myeven))

print(next(myeven))

-----------------------------------------------------------------------
"""""    TopTen Nos. squares    """""

def topten(n):
    print('starting from here squares are :')
    n = 1
    while n <=10:
        square = n*n
        yield square
        n = n + 1
        
top_tens = topten('n')
print(next(top_tens))


for item in top_tens:
    print(item)

---------------------------------------

"""
Code Challenge
Write a generator which computes the running average from the list
[7, 13, 17, 231, 12, 8, 3]
"""

list1 = [7, 13, 17, 231, 12, 8, 3]

def avg_num(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    avg = sum/(len(list1))
    yield avg
   
Average = avg_num(list1)
print(type(Average))

print(next(Average))

##############  OR   #####################

list1 = [7, 13, 17, 231, 12, 8, 3]

def avg_num(list1):
    sum = 0
    for i in list1:
        sum = sum + i
    avg = sum/(len(list1))
    yield avg

Average = avg_num(list1)
print(next(Average))

# print(next("{0.2f}".format(Average))
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















































































































    










































    
    
    
    
    
    
    
    
    
    
    















 
    
