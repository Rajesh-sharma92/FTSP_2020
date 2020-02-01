# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:22:25 2020

@author: Rajesh
"""

" pg : (31) WAP to print this below pattern."

            1234
             123
              12
               1
n = int(input('Enter n value :'))
for i in range(n): # 0,1,2,3
    print(' '*(i), end='')
    for j in range(n-i):
        print((j+1) , end='')
    print()
    
" pg : (32) WAP to print this below pattern."

    DDDD
     CCC
      BB
       A
       
n = int(input('Enter n value :'))
for i in range(n): # 0,1,2,3
    print(' '*(i) , chr(65+n-i-1)*(n-i))
    print()
    
" pg : (33) WAP to print this below pattern."

            ABCD
             ABC
              AB
               A
   
n = int(input('Enter n value :'))
for i in range(n): # 0,1,2,3
    print(' '*(i) , end='')
    for j in range(n-i):
        print(chr(65+j) , end='')
    print()
    
" pg : (34) WAP to print this below pattern."

            *
           ***
          *****
         *******
        
n = int(input('Enter n value :'))
for i in range(n): # 0,1,2,3
    print(' '*(n-i-1) , '*'*(2*i+1))
    
" pg : (35) WAP to print this below pattern."

                1
               222
              33333
             4444444
             
n = int(input('Enter n value :'))
for i in range(n): # 0,1,2,3
    print(' '*(n-i-1) , str(i+1)*(2*i+1))

" pg : (36) WAP to print this below pattern."

                1
               333
              55555
             7777777

n = int(input('Enter n value :'))
for i in range(n): # 0,1,2,3
    print(' '*(n-i-1) , str(2*i+1)*(2*i+1))
    

    



    
    







    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
