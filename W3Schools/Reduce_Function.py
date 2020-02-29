# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 10:30:02 2020

@author: Rajesh
"""
Reduce Function :-
---------------
It always perform the given task as defined in the reduce function and calculate the same and 
gives the output in the single number.

NOTE :- To use the reduce function always we need to import the reduce the function from functools.

from functools import reduce

list1 = [1,2,3,4,5]
reduce(lambda x , y : x+y , list1) # 15

list2 = [10,20,30,40,50]
reduce(lambda a,b : a+b , list2)# 150

list3 = [10.5,20.5,30.5,40,80]
reduce(lambda x,y : x+y , list3)

str1 = 'Rajesh','sharma','forsk'
reduce(lambda x,y : x+y , str1)

# using reduce to compute maximum element from list.

list1  = [ 1 , 3, 5, 6, 2, ] 
reduce(lambda x,y : x if x > y else y , list1) # 6

# using reduce to compute minimum element from list.
list1  = [20,30,4,50,80,100] 
reduce(lambda x,y : x if x < y else y , list1) # 4
---------------------------------------------------------------------------------------------------
NOTE :- Pls add all the given nos. present in the list without using Lambda functions.
Yes. We can do it by using the Operator functions.
 
from functools import reduce

import operator

list1  = [1,3,5,6,2] 
reduce(operator.add , list1)

list1  = [1,3,5,6,2] 
reduce(operator.mul ,list1) # 180

list1 = [20,30,10,50,70]
reduce(operator.sub , list1) # -140

str1 = 'Forsk Coding'
str2 = 'school Jaipur'

reduce(operator.add , [str1,str2])

# using reduce to concatenate string.
reduce(operator.add , ['Forsk','Coding','school','Jaipur'])

reduce(operator.add,['Rajesh','sharma'])































