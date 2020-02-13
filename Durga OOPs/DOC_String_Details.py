# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:47:36 2020

@author: Rajesh
"""

class Employee:
    ''' This class is developed by Mr. "Rajesh sharma" and 
    It stored the very useful information into it. '''
    
    pass 
    
print(Employee.__doc__)
 
help(Employee)

-----------------------------------------------------------------------------

class student:
    ''' This is student class and It provides the student details. 
    student_name = ' Rajesh sharma from forsk school '
    
    '''
    pass

print(student.__doc__)
    
help(student)
--------------------------------------------------------------

class student1:
    ''' THIS CLASS IS USED FOR STUDENT DETAILS.'''
    
def __init___(self):
    print(id(self))
    
s = student1()
print(id(s))
    
if s==(self):
    print('True')
else:
    print('False')
--------------------------------------------------------------------------
e1 = Employee(eno=100,ename='Rajesh',esal=1000,eaddr='jaipur')
----------------------------------------------------------------------------

NOTE :- We can use any word instead self and it need to access through that words only all 
instances variables. internally it will be taking the self variable and for the x variable.



class Employee:
    '''doc string(description)'''
    def __init__(s,eno,ename,esal,eaddr):
        s.eno = eno
        s.ename = ename
        s.esal = esal
        s.eaddr = eaddr
        
    def info(x):
        print('*'*25)
        print('Employee number :', x.eno)
        print('Employee name :', x.ename)
        print('Employee salary :', x.esal)
        print('Employee address :', x.eaddr)
        #print('*'*20)
            
e1 = Employee(100,'Rajesh',10000,'sikar')
e2 = Employee(200,'sharma',20000,'jaipur')

e1.info()
e2.info()



















