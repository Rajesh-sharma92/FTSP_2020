# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:59:31 2020

@author: Rajesh
"""
How to handle CSV files :-
-----------------------
csv ---> Comma seperated values.

Writing data to csv files :-
-------------------------
import csv
# with open('E:/Durga OOPs/students.csv','w') as f: # Here always blenk lines will be there.
with open('E:/Durga OOPs/students.csv','w',newline='') as f:   # If new line = '' it replaces the space .
    w = csv.writer(f)
    w.writerow(['NAME','ROLLNO','MARKS','ADDRESS']) # Automatically Row Header create.
    while(True): # Infinite Lop
        name = input('Enter Student Name :')
        rollno = int(input('Enter Student RollNo :'))
        marks = int(input('Enter Student Marks :'))
        address = input('Enter Student Address :')
        w.writerow([name,rollno,marks,address])
        option = input('Do you want to Insert one more record[Yes|No] :')
        if option.lower() == 'no':
            break
print('Total Students data written to csv file successfully')
-----------------------------------------------------------------------------------------------------

How to Read CSV files :-
----------------------
import csv
f = open('E:/Durga OOPs/students.csv','r')
r = csv.reader(f)
data = list(r)
print(data)

for row in data:
    for column in row:
        print(column , '\t' , end='')
    print()
    
--------------------------------------------------------------------------------------------
for row in data:
    print(row[0],row[1],row[2],row[3] , sep='\t')
    
************* Result ***************
      
NAME    ROLLNO  MARKS   ADDRESS
Rajesh  1001    65      sikar
sandeep 1002    85      Ajmer
yogi    1003    99      delhi
sharma  1004    100     Bangalore
  
      
       
        
    
    



















