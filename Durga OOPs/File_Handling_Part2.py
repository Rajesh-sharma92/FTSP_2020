# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:17:42 2020

@author: Rajesh
"""

File Handling :- There are 2 more important methods.
-------------
1) tell()
2) seek()
---------------------------------------------------------------------------------------
1) tell():- To return the current position of the cursor(file pointer) from begining
of the file.
It always shows the zero index in the file like list , tuple and etc.

NOTE :- If there cursors are avilable in the files in different modes like.
r mode ---> begin 
w mode ---> begin
a mode ---> last

f = open('E:/Durga OOPs/Files Handling/tell_Details.txt','r')
print('The cursor position in the file in Read mode :', f.tell())
print(f.read(2))
print('The cursor position in the file in Read mode :', f.tell())

************ Result ***********
The cursor position in the file in Read mode : 0
RA
The cursor position in the file in Read mode : 2

-----------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/tell_Details.txt','w')
print('The cursor position in the file in Read mode :', f.tell())
print(f.write('bangalore'))
print('The cursor position in the file in Read mode :', f.tell())

************ Result ***********
The cursor position in the file in Read mode : 0
9
The cursor position in the file in Read mode : 9

--------------------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/tell_Details.txt','a')
print('The cursor position in the file in Read mode :', f.tell())
print(f.write('bangalore \n'))
print('The cursor position in the file in Read mode :', f.tell())

************ Result ***********
The cursor position in the file in Read mode : 9
11
The cursor position in the file in Read mode : 21
------------------------------------------------------------------------------------------------
2) seek() :- To move the cursor to at specified location in the file.
NOTE :- It will take to your cursor at specified location but always from begining of the file.
like seek(0) --> 0
seek(17) --> from 0 to 17 position
Ex :-

f = open('E:/Durga OOPs/Files Handling/seek_Details.txt','w')
data = 'All students are STUPIDS'
f.write(data)
-------------------------------------------------------------------------------
with open('E:/Durga OOPs/Files Handling/seek_Details.txt','r+') as f:
    text = f.read()
    print(text)
    print('The current position :', f.tell())
    f.seek(17)
    print('The current position :', f.tell())
    f.write('GEMS!!!')
    f.seek(0)
    text = f.read()
    print('Data After Modification')
    print(text)

************ Result ***********
All students are STUPIDS
The current position : 24
The current position : 17
Data After Modification
All students are GEMS!!!    
------------------------------------------------------------------------------------------
NOTE :- If we will try to use the 'r+' mode then first we need to read the data from file
and then write the data into file. but if i will go for directly for write operation then
Cursor will be at begining position and It will be adding at begining the data into the file.

f = open('E:/Durga OOPs/Files Handling/seek_Details.txt','w')
data = 'All students are STUPIDS'
f.write(data)
with open('E:/Durga OOPs/Files Handling/seek_Details.txt','r+') as f:
    f.write('Data')
    print(data)
************ Result ***********
DataAll students are STUPIDS
-----------------------------------------------------------------------------------------
NOTE :- f.seek(-17) ValueError: negative seek position -17
seek() method always takes index from 0 only. It will not consider any -ve index.
NOTE :- seek() method always takes +ve numbers only. like
seek(17) , seek(10) , seek(0)
-----------------------------------------------------------------------------------------
f = open('E:/Durga OOPs/Files Handling/seek_Details.txt','w')
data = 'All students are STUPIDS'
f.write(data)
with open('E:/Durga OOPs/Files Handling/seek_Details.txt','r+') as f:
    f.seek(1000)
    f.write('RAJESH SHARMA')
    print('The current position :', f.tell())
    
************ Result ***********
The current position : 1013
----------------------------------------------------------------------------------------------
os 
isfile()

function vs. method :-
-------------------
The functions are declared inside a class are called as methods.

The things which are declared outside of the class are called as functions.

NOTE :- As we can say that Python is function & OOPs language.
functional ==> Functions
Object Oriented ==> Methods

Question :- WAP to check wheather the given file exists or not ? If it is available 
then print its contents.
Answer :- Yes, we can do it by using the " os " library. 

import os
fname = input('enter the filename :')
if os.path.isfile(fname):
    print('File Exists :', fname)
    f = open(fname,'r')
    print('The Contents of the file :')
    print(f.read())
else:
    print('File Does not Exists :', fname)
    
*********** Result *********
It will be showing the all contents present into that file.
--------------------------------------------------------------------------------------------------
Question :- WAP to print the no. of lines , words and characters present in the given file.
Answer :- No. of lines = 5
No. of words = 20
No. of characters = 124

import os
fname = input('enter the filename :')
if os.path.isfile(fname):
    print('File Exists :', fname)
    f = open(fname,'r')
    lcount=wcount=ccount=0
    for line in f:
        lcount = lcount+1
        words = line.split()
        wcount = wcount+len(words)
        ccount = ccount+len(line)
    print('The No. of lines are :', lcount)
    print('The No. of Words are :', wcount)
    print('The No. of Characters are :', ccount)
else:
    print('File does not Exists :', fname)    

************* Result ***************
No. of lines = 5
No. of words = 20
No. of characters = 124

NOTE :- File name is " FileDeatils.txt "
------------------------------------------------------------------------------------
How to Handle Binary Data :-
-------------------------
Images ,vedios,files and Audios files.

f1 = open('E:/Durga OOPs/Files Handling/images.jpg','rb')
f2 = open('E:/Durga OOPs/Files Handling/NewGuidoFile.jpg','wb')
b = f1.read()
f2.write(b)
f1.close()
f2.close()

print('NeW Image is avilable : NewGuidoFile.jpg')

---------------------------------------------------------------------------------------
How to read & write the mp4 files.

f1 = open('E:/Durga OOPs/Files Handling/images.mp4','rb')
f2 = open('E:/Durga OOPs/Files Handling/NewGuidoFile.mp4','wb')
b = f1.read()
f2.write(b)
f1.close()
f2.close()
print('NeW Image is avilable : NewGuidoFile.jpg')
------------------------------------------------------------------------------------
NOTE :- pdf files are internally works as binary files only. This above approach 
will be working.


































    

        
        
    




    
  
    
    





























































