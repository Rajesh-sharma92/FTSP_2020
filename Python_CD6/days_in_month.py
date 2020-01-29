# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:13:09 2020

@author: Rajesh
"""

'''Hands On'''
# Make a function days_in_month to return the number of days in a specific month of a year. 


month = input('Enter any of the month Name :')

def days_in_month(month):
    
    list1 = ['Janurary','Feburary','March','April','May','June','July','August','September','October','November','December']
    
    list2 = [31 , 29 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31 ]
    
    if month in list1:
        
       print(list2[list1.index(month)])
    
print('The no. of days are in month \n ')

days_in_month(month)







































inp = input("Enter month: ")
def days_in_month():
    
    
    list1 =["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"] 
    list2 =[31,29,31,30,31,30,31,31,30,31,30,31]
    if inp in list1:
        print(list2[list1.index(inp)])
days_in_month()
