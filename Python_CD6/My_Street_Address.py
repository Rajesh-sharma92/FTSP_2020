# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:15:17 2020

@author: Rajesh
"""

'''Hands On'''
"""
# Take your street address and make it a list variable myaddress
# where each token is an element.

# What would be the code to set the sum of the numerical portions of
# your address list to a variable called address sum?

# What would be the code to change one of the string elements of the
# list to another string (e.g., if your address had "West" in it, how would
# you change that string to "North")?

# Change the street portion of myaddress to have the street first 
# and the building number at the end. 
          
"""

street_address=input('Enter your home Address \n ')
my_address=street_address.split()
print('My Home Address :', my_address)

# 312 First Street Apartment 11, Onesville, California, 2020 , United States.

   # # SUM printing.

street_address=input('Enter your home Address \n ')
my_address=street_address.split()
sum=0
for item in my_address:
    if item.isnumeric():
        sum=sum+int(item)
print('The sum of All Numeric numbers are :', sum)
        
  # 312 First Street Apartment 11, West  California, 2020 , United States. 
     
street_address=input('Enter your home Address \n ')
my_address=street_address.split()
for item in my_address:
    if item == 'West':
        a = my_address.index("West")
        my_address[a] = "North"

        ### OR #####

street_address=input('Enter your home Address \n ')
my_address=street_address.split()
if "West" in my_address:
    a = my_address.index("West")
    my_address[a] = "North"


street_address=input('Enter your home Address \n ')
my_address=street_address.split()
my_address.remove('KhauStreet')
my_address.remove('300')
my_address.insert(0,'KhauStreet')
my_address.append(300)
print(my_address)

 
    

   













