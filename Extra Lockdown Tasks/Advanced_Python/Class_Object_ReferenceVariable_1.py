# Class :- 
# plan , design , template , blueprint.
# start constructing the building.
# implmentation is nothing objects .

# Object  :- Physaical items. 

# Reference Variable :- 

# OOPs :- Object oriented Programming Lang.

class Employee:
    ''' This class is Employee class '''
    
    def __init__(self,empid,ename): # Contrusctor
        self.empid = empid
        self.ename = ename
        
    def details(self):
        print('The Emp ID :', self.empid)
        print('The Emp Name :', self.ename)
 
e1 = Employee(1001,'Andy') # object creation.
e1.details()
e2 = Employee(2002,'Candy')
e2.details()      

print(e2.empid)
print(e2.ename)

 
print(Employee.__doc__)
help(Employee)
    





