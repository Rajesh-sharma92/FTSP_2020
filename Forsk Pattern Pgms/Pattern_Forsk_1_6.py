# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:07:44 2020

@author: Rajesh
"""

" pg : (1) WAP to print this below pattern."

        * * * * 
        * * * * 
        * * * * 
        * * * * 
        
n = int(input('Enter the number of rows :'))

for i  in range(n):
    
    print('* ' * (n))


" pg : (2) WAP to print this below pattern."

            1 1 1 1 
            2 2 2 2 
            3 3 3 3 
            4 4 4 4
            
n = int(input('Enter n value :'))

for i in range(n):
    
    print((str(i+1)+' ') * n)
    
   
 " pg : (3) WAP to print this below pattern."   
 
            1 2 3 4 
            1 2 3 4 
            1 2 3 4 
            1 2 3 4 
             
 
n = int(input('Enter n value :'))
 
for i in range(n): # 0,1,2,3
    
    for j in range(n): # 0,1,2,3
        
        print(j+1 , end=' ')
        
    print()
  

" pg : (4) WAP to print this below pattern."   

            6 7 8 9 
            6 7 8 9 
            6 7 8 9 
            6 7 8 9 
            
n = int(input('Enter n value : '))

for i in range(n):
    
    x = 6
    
    for j in range(n):
        
        print(x , end =' ')
        
        x = x + 1
        
    print()
        
" pg : (5) WAP to print this below pattern."  
            
            AAAA
            BBBB
            CCCC
            DDDD 

n = int(input('Enter n value :'))
for i in range(n):
    print(chr(65+i)*n)

" pg : (6) WAP to print this below pattern."  

        A B C D 
        A B C D 
        A B C D 
        A B C D 

n = int(input('Enter n value :'))
for i in range(n):
    for j in range(n):
        print(chr(65+j) , end=' ')
    print()



#################### END #################################
    
    







    
    
    
    
    
    
    
















    
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





    
    
        
         
         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    