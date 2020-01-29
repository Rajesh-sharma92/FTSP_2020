# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:25:30 2020

@author: Rajesh
"""
'''Hands On'''
# Create a list of Fibonnaci numbers up to the 50th term.
# The program will then ask the user for which position in the sequence
# they want to know the Fibonacci value for
# The Fibonacci sequence was originally used as a basic model for rabbit population growth:  


a , b = 0 , 1

while b < 50:
    
    print(b)
    
    a , b = b , a + b
    
   
print('The 50th Term in Fibbonocci Series :', b) -- O/P :- 55


'''Hands On'''
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.

words = ['aba', 'xyz','aa', 'x', 'bbb']
#words = ['', 'x', 'xy', 'xyx', 'xx']
#words = ['aaa', 'be', 'abc', 'hello']


for item in words:
    
    if item[0]==item[-1] and len(item)>=2:
        print(item)
        
        item=item.count(item)
        print(cnt)
        
        








