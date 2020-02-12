# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:40:42 2020

@author: Rajesh
"""

class student:
    ''' This class is developed by Mr. Rajesh sharma '''
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
        
    def talk(self):
        print('Hello My name is :',self.name)
        print('Hello My rollno is :',self.rollno)

s = student(100,'sunny')
#print(s.name)
#print(s.rollno)
s.talk()

s1 = student(200,'Bunny')
s1.talk()

s2 = student(300,'Chinny')
s2.talk()

"""
NOTE :- student ==> class.
        Objects ==> student(arguments)
        s ==> 's' is nothing but reference variable.
"""












