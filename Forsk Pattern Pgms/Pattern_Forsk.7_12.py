# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:07:44 2020

@author: Rajesh
"""


" pg : (7) WAP to print this below pattern." 

            4 4 4 4 
            3 3 3 3 
            2 2 2 2 
            1 1 1 1  
            
n = int(input('Enter n value :'))
for i in range(n):
    print((str(n-i)+' ')*n)
print()


" pg : (8) WAP to print this below pattern." 

            4 3 2 1 
            4 3 2 1 
            4 3 2 1 
            4 3 2 1 

n = int(input('Enter n value :'))
for i in range(n):
    for j in range(n):
        print((n-j) , end=' ')
        
    print()
    
    
" pg : (9) WAP to print this below pattern." 
            D D D D 
            C C C C 
            B B B B 
            A A A A 
            
n = int(input('Enter n value :'))
for i in range(n):
    print((chr(68-i)+' ')*n)
print()       
  
  
" pg : (10) WAP to print this below pattern."  

            D C B A 
            D C B A 
            D C B A 
            D C B A 
              
n = int(input('Enter n value :'))
for i in range(n):
    for j in range(n):
        print(chr(68-j) , end=' ')
    print()
 
    
" pg : (11) WAP to print this below pattern." 

        *     
        * *    
        * * *   
        * * * *  

n = int(input('Enter n value :'))
for i in range(n):
    print('* '*(i+1) , (' '*(n-i-1)))
print()


" pg : (12) WAP to print this below pattern."  

            1    
            22   
            333  
            4444   

n = int(input('Enter n value :'))
for i in range(n):
    print(str(i+1)*(i+1) , (''*(n-i-1)))
print()

" pg : (13) WAP to print this below pattern."  

            1 
            1 2 
            1 2 3 
            1 2 3 4 
            
n = int(input('Enter n value :'))
for i in range(n):
    for j in range(i+1):
        print(str(j+1) , (''*(n-i-1)) , end='')
    print()



################## END #################
    
    









    
    
    
    
    
    
    
















    
##########################
  
n=int(input())
for i in range(n):
    print(i+1 , end='')
    
    
 ###################

def f1(x,y):
    return x>y

n = input()
arr = map(int, input(f1).split())
    
####################

a = int(input())
b=input().split()
c=[]
for i in b:
    i = int(i)
    c.append(i)





    
    
        
         
         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    