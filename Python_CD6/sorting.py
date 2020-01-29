# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:00:36 2020

@author: Rajesh
"""

"""
Name: 
    Sorting         
Filename:
    sorting.py
Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score 
  
Hint: 
    Not Available 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
Sample Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]

"""

name = ['John','Jony','Jony','Json','Tom']

age = [10,15,20,25,30]

height = [5,6,7,5,6]

tp = zip(name,age,height)

print(tuple(tp))


############### OR ############

for i in range(3):
    
    (name,age,height)=tuple(input("Enter name , age and score :"))
    
    tp = zip(name,age,height)

    print(tuple(tp))
    
    
    
    






