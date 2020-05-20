# Objects , Classes , Reference Variables in Python :- 
 Ex :- Building .---> Classes
 Ex :- ready building means === Objects

class Emp: # class creation
    
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename
        
    def info(self):
        print('The EmpId :', self.eid)
        print('The Name :', self.ename)
        
        
e1 = Emp(1001,'Candy') # object creation

e1.info()


e2 = Emp(2002,'Andy')

e2.info()

    




