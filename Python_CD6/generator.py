# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:46:18 2020

@author: Rajesh
"""


"""
Name: 
    generator       
Filename:
    generator.py 
Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers. 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    2, 4, 7, 8, 9, 12
Sample Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '12')
""" 

" NOTE :- split() function always split the given string and stored the values into list."

s = input('Enter some value :').split(',')

print('The List :', s)


print('The Tuple :', tuple(s))


############# OR ############### 



str1 = input('enter any number :').split()

print('List :', str1)

print('Tuple :', tuple(str1))



