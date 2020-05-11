# What are Keyworded & **kwargs :- 
Ex:- 
def emp(ename,age): # Creation
    print(ename)
    print(age)
    
emp('Ram',25) # Calling

Ex :- 
def emp(ename,**details):
    print('ename :', ename)
    # print('Details :', details)
    
    '''
    for i in details.keys():
        print(i)
    
    
    for j in details.values():
        print(j)
     '''
    for i,j in details.items():
         print(i,j)
     
emp('Ram',eage=25,ecity='Goa',emob=808855)




