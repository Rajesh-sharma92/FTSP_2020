# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:55:45 2020

@author: Rajesh
"""
File Handling :- 
-------------
Parmanantly storage for future purpose.

Temporary storage means list , tuple . set and dictionary data will stored sort period of time and once the
program has been executed then data will be gone after that.

l = [] # empty list
n = int(input('Enter the vaule of n :'))
for i in range(n):
    x = input('Enter the values :')
    l.append(x)
print(l)

*************** Result ****************
Enter the vaule of n :3

Enter the values :Rajesh

Enter the values :sandeep

Enter the values :Brijmohan
['Rajesh', 'sandeep', 'Brijmohan']
------------------------------------------------------------------------
Enter the vaule of n :3

Enter the values :Sachin

Enter the values :Yuvraj

Enter the values :Dhoni
['Sachin', 'Yuvraj', 'Dhoni']

NOTE :- We can say that in the above example there are data is not stored as parmanantlly and it is 
just stored as Temporary storage only means once the program gets executed data will be gone.

NOTE :- We can not use such kind of data in the future and it is used for sort period of time is 
called as Temporary storage.

--------------------------------------------------------------------------------------------------------------
Parmanent storage :- Files and Database Concepts.
-----------------
Files :- If we want to store less amount of data then better to go for Files concepts.
Ex :- For one online class total no. of students are 150 only then better to go for file concept.

DataBase :- If we want to store Huge amount of data then better to go for Database Concepts.
Ex :- For any Bank consider there are 1 lakhs customers then better to go for Database concept.

NOTE :- some of the time Facebook , twitter and etc. companies data are very very huge data as per like
comments , posts and tweets to store all these data companies will go for Big Data , Hadoop Techniques.
----------------------------------------------------------------------------------------------------------------------
Files :- There are 2 types of files.
-----
1) Text Files :- Text data like name of students , marks of students.
2) Binary Files :- Images , vedio files , Audio files and etc.
------------------------------------------------------------------------------------------------
Read / Write files ----> First we need to open before doing any operation on it.

open(filename,mode)
where filename means name of the file and path 
mode means like read,write and append

Ex :- To open abc.txt file for write opearion
f = open('abc.txt','w')

The allowed modes are in python :-
--------------------------------
1) Read mode 
2) Write mode
3) Appened mode
  
1) r     
2) w
3) a
4) r+
5) w+
6) a+
7) x
--------------------------------------------------------------------------------------------------------
1) r :- read mmode. 
    open an existing file for read operation. If the specified file is not available then we will
    get an error like FileNotFoundError. 
        
NOTE :- Default mode of any file is read operation only.
f = open('abc.txt') # Here we have not mentioned the mode so it will be taking Read mode as default.
f = open('abc','r') ---> Read mode
----------------------------------------------------------------------------------------------------------
2) w :- write mode.
   f = open('abc.txt','w')    
open abc.txt file for write operation
If the specified file not available then this line will created the new file with the name of abc.txt
Question :- If the file already contain some data then write operation will be overwrite that data or appened the datat
Answer :- It will be overiding / overwriting the previous data.
------------------------------------------------------------------------------------------------------------------
2) a :- append mode.
    f = open('abc','a')
NOTE :- Here for example if abc.txt file already contains some data and then we are performing the 
append operation then first old data and after that continuation of that data.
NOTE :- Here also if the file not available it will create the new file as write operation and 
but it will not overwrite the data.
---------------------------------------------------------------------------------------------------------------
4) r+ :- first read then write operation
NOTE :- Here always cursor will be at starting of the page and then it will be writing data.
------------------------------------------------------------------------------------------------
5) w+ :- first write then read operation.
NOTE :- It will overwriting the existing data.
--------------------------------------------------------------------------------------------------
6) a+ :- first append then read operation.
NOTE :- It will not overwriting the existing data.  
-----------------------------------------------------------------------------------------------------
7) x :- Exclusive mode.
  It is used for write operation.  
  f = open('abc.txt','w')
  
File may or may not exists :-
--------------------------
f = open('abc.txt','x')
Compulsory file should not be available.
If abc.txt file already available then we will get an error like FileExistsError
NOTE :- All these above modes are available for text files only.
LIKE r,w,a,r+,w+,a+,x 
----------------------------------------------------------------------------------------------------------------
For binary files there are 7 modes are available :- All modes ends with b means binary files.
------------------------------------------------
rb , wb , ab , r+b , w+b , a+b , xb
NOTE :- All these above modes are case sensitive only we need to use in the lower case not upper case.
---------------------------------------------------------------------------------------------------------------
Open the file .... name of the ....mode of the file
f = open('abc.txt','r')
... perfromed required read operation
always we need to close the file.
f.close()

NOTE :- If you do not close file nothing will be happen but it is not the good practice for good engineer.
Without closing also we can perform our task at the certain period of time there will be performance
issue with the system like Too many files are opened.

NOTE :- To perform any kind of operations  and after that we need to close the file and it is 
the very good practice for great performance.
---------------------------------------------------------------------------------------------------------
f = open('abc.txt','r')

where f is the file object

various properties of file object :-
---------------------------------
f.name
f.mode
f.closed

NOTE :- All these above 3 are variables or attributes.

f.readable()
f.writable()

NOTE :- Above 2 are methods and return the boolean values true & false.
------------------------------------------------------------------------------------------------------------------------------
Ex :- This is the simple example.

f = open('E:/Durga OOPs/Files Handling/abc.txt','r')
# f = open('E:/Durga OOPs/Files Handling/abc.txt') # default mode is read mode only.
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************
File name : E:/Durga OOPs/Files Handling/abc.txt
File mode : r
Is file Readable ? : True
Is file writable ? : False
Is file closed ? : False
Is file closed ? : True
-------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/abc.txt','w')
# f = open('E:/Durga OOPs/Files Handling/Test.txt','w')
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************
File name : E:/Durga OOPs/Files Handling/abc.txt
File mode : w
Is file Readable ? : False
Is file writable ? : True
Is file closed ? : False
Is file closed ? : True
------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/abc.txt','a')
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************
File name : E:/Durga OOPs/Files Handling/abc.txt
File mode : a
Is file Readable ? : False
Is file writable ? : True
Is file closed ? : False
Is file closed ? : True
----------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/abc.txt','r+')
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************
File name : E:/Durga OOPs/Files Handling/abc.txt
File mode : r+
Is file Readable ? : True
Is file writable ? : True
Is file closed ? : False
Is file closed ? : True
--------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/abc.txt','w+')
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************
File name : E:/Durga OOPs/Files Handling/abc.txt
File mode : w+
Is file Readable ? : True
Is file writable ? : True
Is file closed ? : False
Is file closed ? : True
--------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/abc.txt','a+')
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************
File name : E:/Durga OOPs/Files Handling/abc.txt
File mode : a+
Is file Readable ? : True
Is file writable ? : True
Is file closed ? : False
Is file closed ? : True
-----------------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/abc.txt','x')
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************

FileExistsError: [Errno 17] File exists: 'E:/Durga OOPs/Files Handling/abc.txt'

--------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/abcd.txt','x')
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************
File name : E:/Durga OOPs/Files Handling/abcd.txt
File mode : x
Is file Readable ? : False
Is file writable ? : True
Is file closed ? : False
Is file closed ? : True

NOTE :- Can I Run this above ile fagain ? Yes. you can run but you will be getting an error like
FileExitsError on console. Coz file is already there then why to create again No use at all.
------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/xyz.txt','r')
print('File name :', f.name)
print('File mode :', f.mode)
print('Is file Readable ? :', f.readable())
print('Is file writable ? :', f.writable())
print('Is file closed ? :', f.closed)
f.close()
print('Is file closed ? :', f.closed)

*********** Result *************
FileNotFoundError: [Errno 2] No such file or directory: 'E:/Durga OOPs/Files Handling/xyz.txt'
----------------------------------------------------------------------------------------------------------

Writing data to a file :- There are 2 ways to write data into a file. 
----------------------
f.write(str)
f.writelines(list of lines)

where str means some single string data.
where list of lines means group od strings data like list,tuple,set and dict.

f = open('E:/Durga OOPs/Files Handling/xyz1.txt','w')
f.write('Forsk')
f.write('Coding')
f.write('school jaipur')
f.close()
print('Write operation has been completed')
---------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/xyz1.txt','w')
f.write('Durga \n')
f.write('software \n')
f.write('solutions \n')

f.close()
print('Write operation has been completed')
-----------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/xyz1.txt','a')
f.write('Durga \n')
f.write('software \n')
f.write('solutions \n')

f.close()
print('Append operation has been completed')
-------------------------------------------------------------------------------------------------------------
NOTE :- The most commonly used data mode is read mode only coz as a programmer we need to read 
the data most of the time from different kind of files and performs some operations.

NOTE :- Here f is object reference for file and we can use any variables but it is easy to related
to the file and easy to understand by everyone. 
-------------------------------------------------------------------------------------------------------
f.writelines(list of lines)

f = open('E:/Durga OOPs/Files Handling/xyz2.txt','w')
l = ['sunny','bunny','chinny','vinny'] # here data will be in a single line default.
f.writelines(l)
f.close()
print('Write Operation Completed')
------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/xyz2.txt','w')
l = ['sunny\n','bunny\n','chinny\n','vinny\n'] # here pls give \n in data then it will be in the next lines.
f.writelines(l)
f.close()
print('Write Operation Completed from list')
---------------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/xyz2.txt','w')
t = ('sunny\n','bunny\n','chinny\n','vinny\n') # here pls give \n in data then it will be in the next lines.
f.writelines(t)
f.close()
print('Write Operation Completed from tuple')

NOTE :- Here we can see that tuple and all present strings are added only once into the file.
Tuples are Immutable in Python.We can not add anything to it once declared.
--------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/xyz2.txt','w')
t = {'sunny\n','bunny\n','chinny\n','vinny\n'} # here pls give \n in data then it will be in the next lines.
f.writelines(t)
f.close()
print('Write Operation Completed from set')
------------------------------------------------------------------------------------------------------------
Question :- Write some data to some file ?
file name i will pass as dynamic input.
Data can entered as dynamic input ?

Answer :- 
NOTE :- \n any back slash charatcetr is there and It always represents the escape character.
Ex :-
fname = input('Enter file name :')
f = open('E:\\Durga OOPs\\Files Handling\\' +fname ,'w')
feedback = input('Enter your Feedback data :')
f.write(feedback)
f.close()
print('Write Operation has been completed')
-------------------------------------------------------------------------------------------------------
Ex :-
fname = input('Enter file name :')
f = open('E:/Durga OOPs/Files Handling/' +fname ,'w')
feedback = input('Enter your Feedback data :')
f.write(feedback)
f.close()
print('Write Operation has been completed')
----------------------------------------------------------------------------------------------------
fname = input('Enter file name :')
f = open('E:/Durga OOPs/Files Handling/' +fname ,'a')
n = input('Enter No. of feedbacks :')
n = int(n)
for i in range(n):
    i = input('Pls enter all the details as per feedback :')
    f.write(i)
f.close()
print('Write Operation has been completed')
---------------------------------------------------------------------------------------------------------------

Redaing character data from the text files :-
------------------------------------------
f.read() ==> To Read total data from file.
f.read(n) ==> To Read n characters from the file.
f.readline() ==> To read only one line.[NOTE :- First time first line , second time scond line and etc.]
f.readlines() ==> To read all lines into a list.
Ex :- 
f = open('E:/Durga OOPs/Files Handling/xyz2.txt','r')
data = f.read()
print(data)
******* Result ************
chinny
sunny
bunny
vinny
---------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/simple.txt')  # Default mode is read only.
data = f.read()
print(data)
******* Result ************
"""" FORSK CODING SCHOOL IN SITAPURA JAIPUR """.
----------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/simple.txt')  # Default mode is read only.
data = f.read(10) # It reads only 10 characters from file.
print(data)
******* Result ************
' """" FORSK
----------------------------------------------------------------------------------------------------
Question :- How to read line by line from a file ?
Answer :- By using readline() method of file class.

f = open('E:/Durga OOPs/Files Handling/xyz2.txt','r')
line = f.readline()
print(line)

line = f.readline()
print(line)

******* Result *************
chinny

sunny

NOTE :- readline() method always add the back slash \n automatically in the file.
-----------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/xyz2.txt','r')
line = f.readline()
print(line , end='')

line = f.readline()
print(line, end='')

******* Result *************
chinny
sunny
--------------------------------------------------------------------------------------------------------------
Question :- How to read all the lines from a file ?
Answer :- By using readlines() method of file class.
Ex :-
f = open('E:/Durga OOPs/Files Handling/xyz2.txt','r')
line = f.readlines() # It reads all data into list form.
print(line)
******* Result *************
['chinny\n', 'sunny\n', 'bunny\n', 'vinny\n']

f = open('E:/Durga OOPs/Files Handling/xyz2.txt','r')
lines = f.readlines()
for line in lines:
    print(line , end='')

******* Result *************
chinny
sunny
bunny
vinny
----------------------------------------------------------------------------------------------------
Question :- If we read() method then why do we need the readline() method ?
Answer :- For example if we have 100 customers mobile nos. in a list and we need to read all nos.
from a list one by one. Better to use the readline() method.
-----------------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/xyz2.txt','r')
print(f.read(3))
print(f.readline())
print(f.read(4))
print('The Remainig data :')
print(f.read())

******* Result *************
chi
nny

sunn
The Remainig data :
y
bunny
vinny
------------------------------------------------------------------------------------------------------------
Question :- How to read the data from a file and write into another file like copy operation ?
Answer :- We just need to read the data from a file and we will be copying all the data into it.
Ex :-

f1 = open('E:/Durga OOPs/Files Handling/Input.txt','r')
f2 = open('E:/Durga OOPs/Files Handling/Output.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print('Data Copied from Input.txt file to Output.txt file successfully')

------------------------------------------------------------------------------------------------------------

with Statement :-
--------------
f = open('abc.txt','w')
............
f.close()

------------------------------------------------------------
with open('abc.txt','w') as f: # here No need to close automatically the file.
    ...........
    ........... # Here File will be closed in the with statements.
    ...........
    
NOTE :- If we are using the " with " then automatically file will be closed when with block
completed and  It is Recommanded to use coz sometimes we may forget to close the file.

with open('E:/Durga OOPs/Files Handling/Foesk.txt' ,'w') as f:
    f.write('Forsk \n')
    f.write('Coding \n')
    f.write('School \n')
    print('Is File closed ?:', f.closed) # False
print('Is File closed ?:', f.closed) # True # If with block completed then automatically file will be closed.

*********** Result *************
Is File closed ?: False
Is File closed ?: True
------------------------------------------------------------------------------------------------------
with open('E:/Durga OOPs/Files Handling/FORSK.txt' ,'w') as f:
    f.write('Rajesh sharma \n')
    f.write('From forsk Coding school \n')
    print('Is the file Closed within the with block !!! I think file is not closed after with block file will be closed !!!' ,f.closed)
    
print('Is the file Closed Outside of the with block !!!', f.closed)    
    
*********** Result *************
Is the file Closed within the with block !!! I think file is not closed after with block file will be closed !!! False
Is the file Closed Outside of the with block !!! True
    
NOTE :- We can use " with " keyword with any of the modes. 
NOTE :- It is recommanded for better practice and sometimes we may forget to close the file.
NOTE :- Automatically, Files performance will be increased.
------------------------------------------------------------------------------------------------------------------------------------------
Question :- How to delete the file in python ?
Answer :- Yes, We can do it. 
with open('E:/Durga OOPs/Files Handling/deleted.txt' ,'w') as f: 
    f.write(' """----------This file will be deleted coz we are deleting from our end ----""" ')
    print('Is File closed ?:', f.closed) # False
    
print('Is File closed ?:', f.closed) # True    

import os
os.remove('E:/Durga OOPs/Files Handling/deleted.txt')
print('File has been deleted successfully')
-------------------------------------------------------------------------------------------------------

    
    
    
    
    
    
    
    
    
    
    


































































































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


  
    


























    
























        

    


























    

































