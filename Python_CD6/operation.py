# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:22:24 2020

@author: Rajesh
"""

"""
Name: 
    Operations Function         
Filename:
    operation.py
Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)
Sample Input:
    5,2,6,2,3
Sample Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]
""" 
################ Addition #####################

list1 = input('Enter some numbers from user :').split(',')

def Add(list1):
    j=0
    
    for i in list1:
        j=j+int(i)
    print('sum :',j)
        
Add(list1)

############################## Multiply ########################

list1 = input('Enter some numbers from user :').split(',')

def Multiply(list1):
    j=1
    
    for i in list1:
        j=j*int(i)
    print('Multiplication :',j)
    
Multiply(list1)

######################## Largest #########################

list1 = input('Enter some numbers from user :').split(',')

def Largest(list1):
    
    for i in range(len(list1)-1):
        a=list1[i]
        b=list1[i+1]
        if a<b:
            pass
        else:
            list1[i]=b
            list1[i+1]=a
           
    print('The Largest :', list1[-1])
           
Largest(list1)
    
##################### Smallest #################

list1 = input('Enter some numbers :').split(',')

def Smallest(list1):
    for i in range(len(list1)-1):
        a=list1[i]
        b=list1[i+1]
        if a<b:
            pass
        else:
            list1[i]=b
            list1[i+1]=a
            
    print('Smallest Number :', list1[0])
Smallest(list1)

###################### Sorted #####################

list1 = input('Enter some numbers :').split(',')

def sort(list1):
    
    for i in range(len(list1)-1):
        a=list1[i]
        b=list1[i+1]
        if a<b:
            pass
        else:
            list1[i+1]=a
            list1[i]=b
    print('The Sorted :', sorted(list1))
            
sort(list1)

#################### Without Duplicates ##########################

list1 = input('Enter some numbers :').split(',')

def Without_Duplicates(list1):
    
    set1 = set(list1)
    
    list2 = list(set1)
    
    sorted(list2)
    
    print('The Duplicates :',list2)
    
    Without_Duplicates(list1)


list1 = [10,20,30,40,50]
























