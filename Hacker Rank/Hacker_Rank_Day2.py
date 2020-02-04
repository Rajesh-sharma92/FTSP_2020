# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:32:18 2020

@author: Rajesh
"""

n = int(input())
list = input().split()
b=[]
for i in list:
    c=int(i)
    b.append(c)
    
d=max(b)
e=b.count(d)
for i in range(e):
    b.remove(d)
print(max(b))    



###########################################

n = int(input('Enter n value :'))
a = []
for i in range(n):
    stu_name = input().split()
    a.append(stu_name)
    
   
##############################################
    
n = int(input())

n1 = input().split()

tup1 = tuple(map(int,n1))

res = hash(tup1)

print(res)
    
######################################

x = int (input()) 
y = int (input()) 
z = int (input()) 
n = int (input()) 
ar = [] 
p = 0 
for i in range ( x + 1 ) :
    for j in range( y + 1):  
        for k in range(z+1):
            if i+j+k != n: 
                ar.append([])
                ar[p] = [ i , j , k ] 
                p+=1 
print(ar)
    

























    









