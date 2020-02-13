# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:21:43 2020

@author: Rajesh
"""

class Employee:
    '''doc string(description)'''
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
        
    def info(self):
        print('*'*25)
        print('Employee number :', self.eno)
        print('Employee name :', self.ename)
        print('Employee salary :', self.esal)
        print('Employee address :', self.eaddr)
        #print('*'*20)
            
e1 = Employee(100,'Rajesh',10000,'sikar')
e2 = Employee(200,'sharma',20000,'jaipur')

e1.info()
e2.info()

""" NOTE :- Class ==> Employee.
    
        Employee(100,'Rajesh',10000,'sikar') ==> Object.
        
        e1 , e2 :- are reference variables.
    """
    
    
    
    
    