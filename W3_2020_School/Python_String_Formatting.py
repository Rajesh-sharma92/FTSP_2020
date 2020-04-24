# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:09:57 2020

@author: Rajesh
"""
'''
Python String Formatting :- 
--------------------------
'''
NOTE :- To make sure a string will display as expected, we can format the result with the 
format() method.

String format() :- 
----------------
The format() method allows you to format selected parts of a string.

1) Sometimes there are parts of a text that you do not control, maybe they come from a 
database, or user input?

2) To control such values, add placeholders (curly brackets {}) in the text, and run 
the values through the format() method.

Ex :- Add a placeholder where you want to display the price.

price = 49

str1 = 'The Price is {} dollors'

print(str1.format(price))
----------- Result --------
The Price is 49 dollors

NOTE :- You can add parameters inside the curly brackets to specify how to convert the value.

Ex :- Format the price to be displayed as a number with two decimals.

Rate = 350

str1 = 'The Rate is in {:.2f} in Euros'

print(str1.format(Rate))
----------- Result --------
The Rate is in 350.00 in Euros

Ex :- 

Quanities = 25 

Price = 5

Total_Price = 125

# Total Price how much for each pen = 5*25 = 125/-
 
str1 = 'Each Pen Rate : {} and Quanities are : {} then Total cost : {} in INR'

print(str1.format(Price , Quanities , Total_Price))
----------- Result --------
Each Pen Rate : 5 and Quanities are : 25 then Total cost : 125 in INR


'''
Multiple Values :- 
-----------------
If you want to use more values, just add more values to the format() method.
'''
Ex :- 

quantity = 3
itemno = 'BetterMilk'
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
----------- Result --------
I want 3 pieces of item number BetterMilk for 49.00 dollars.


'''
Index Numbers :-
----------------
You can use index numbers (a number inside the curly brackets {0}) to be sure the values 
are placed in the correct placeholders.
'''
Ex :- 

quantity = 10
itemno = 'Babudaya_special_Pakodi'
price = 150
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
----------- Result --------
I want 10 pieces of item number Babudaya_special_Pakodi for 150.00 dollars.

Ex :- 

quantity = 25
itemno = 'Gududaya_Yummy_Jamun'
price = 45
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
----------- Result --------
I want 25 pieces of item number Gududaya_Yummy_Jamun for 45.00 dollars.


NOTE :- Also, if you want to refer to the same value more than once, use the index number.

Ex :- 

Age = 25
Name = 'Rajesh sharma'
Job = 'Data scientist'

str1 = 'His Name is {1}. {1} is {0} years old and working as a {2} at IBM Bangalore.'

print(str1.format(Age,Name,Job))
----------- Result --------
His Name is Rajesh sharma. Rajesh sharma is 25 years old and working as a Data scientist at IBM Bangalore.
    

'''
Named Indexes :-     
---------------
You can also use named indexes by entering a name inside the curly brackets {carname}, 
but then you must use names when you pass the parameter values txt.format(carname = "Ford").
'''
Ex :- 

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))    
----------- Result --------
I have a Ford, it is a Mustang.   
    

Ex :- 

str1 = 'I just love a girl {Girlname} , and she also loves me {how}.'
print(str1.format(Girlname='Usha_Babudaya_Gududay' , how='lots and lots'))
----------- Result --------
I just love a girl Usha_Babudaya_Gududay , and she also loves me lots and lots.    
    
    
