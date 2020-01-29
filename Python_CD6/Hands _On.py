# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:10:26 2020

@author: Rajesh
"""

'''Hand on'''
# remove all 3 from the list
some_list = [1,2,3,5,65,53,3,4,2,4,3,5,6,7,8,1,2,3]

for item in some_list:
    if item==3:
        some_list.remove(3)
print(some_list)
    

# some_list = [1,2,3,5,6,2,4,3,5,6,7,8,1,2,3]

input_string = input("Enter a list element separated by space ")
some_list  = input_string.split()
a = some_list.count('10')
for item in range(0,a):
    some_list.remove('10')
print(some_list)


'''Hands On'''
# Take the list of the parts of your street address
# Write a loop that goes through that list and prints out each item in that list
myaddress = [3225, 'West', 'Foster', 'Avenue', 'Chicago', 'IL', 60625]


street_address=input('Enter your home Address :')

myaddress=street_address.split()

for item in myaddress:
    print(item)

"""
'''Hands On'''
#Looping through a list of temperatures and applying a test
#Pretend you have the following list of temperatures T:
T = [273.4, 265.5, 277.7, 285.5]
#and a list of flags called Tflags that is initialized to all False
Tflags = [False, False, False, False]
#Write a loop that checks each temperature in T and sets the corresponding
#Tflags element to True if the temperature is above the freezing point of water.
"""

T = [273.4, 265.5, 277.7, 285.5]

Tflags = [False, False, False, False]

n=0

for i in T: 

    if T[n] > 273:

        print('The temperature in T :',T[n])

        print('The temperature is above the freezing point of water :', not Tflags[n])
        
    else:
        
        print('The temperature in T :',T[n])
        print('The temperature is above the freezing point of water :', Tflags[n])
        
    n = n+1
    
 """   
'''Hands On'''
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
"""

s=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

s1=[]
s2=[]
s3=[]

for item in s:
    if item[0]=='x':
        s1.append(item)
        s1.sort()
    else:
        s2.append(item)
        s2.sort()
        s3=s1+s2
        print(s3)
        
        
        
  '''Hands On'''
# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

nums = [1, 2, 2, 3]
#nums = [2, 2, 3, 3, 3]
#nums = []

nums=set(nums) 
nums=list(nums)
print(nums)     
        
        
'''Hands On'''
# Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

list1 = ['aa', 'xx', 'zz'] #['aa', 'xx']         ['aa', 'aa']
list2 = ['bb', 'cc']       #['bb', 'cc', 'zz']   ['aa', 'bb', 'bb']

list2.extend(list1)

list2.sort()

print(list2)

### OR #####

list3=list1+list2
list3.sort()
print(list3)
        
    
"""
'''Hands On'''
#Create a dictionary myaddress using your address. 
#Choose relevant keys(they will probably be strings), 
#and separate your address into street address,
#city, state, and postal code portions, all of which are strings (for your ZIP
#Code, don’t enter it in as a number).
myaddress = {'street':'3225 West Foster Avenue','city':'Chicago', 'state':'IL','zip':'60625'}

"""

myaddress={} # Empty dictionary

myaddress['street']='3225 West Foster Avenue'
myaddress['city']='Chicago'
myaddress['state']='IL'
myaddress['zip']='60625'

for key in myaddress.keys():
    print(key)
    
for value in myaddress.values():
    print(value)
    
for key,value in myaddress.items():
    print(key,value)
    
####### OR ###############

    
dict1 = {"India":"Delhi","USA":"Washington","Russia":"Moscow"}

dict1['Greek'] = 'Athens'


for key in dict1.keys():
    print(key)
        
for value in dict1.values():
    print(value)
    
for key,value in dict1.items():
    print(key,value)    













































    







