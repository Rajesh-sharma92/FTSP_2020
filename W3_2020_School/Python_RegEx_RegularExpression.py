# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:51:42 2020

@author: Rajesh
"""
'''
Python RegEx :- 
-----------------
'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

RegEx Module :- 
---------------
Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

import re


RegEx in Python :- 
-------------------
When you have imported the re module, you can start using regular expressions.

Ex :- Search the string to see if it starts with "The" and ends with "Spain".

import re

str1 = 'The rain in Spain'

x = re.search('^The.*Spain$',str1)

if (x):
  print("YES! We have a match!")
else:
  print("No match")
--------- Result ----------
YES! We have a match!



Ex :- 'Rajesh loves Babudaya and babudaya loves Rajesh'

import re

str1 = 'Rajesh loves Babudaya and babudaya loves lots to Rajesh'

x = re.search('^Rajesh.*Rajesh$', str1)

if x:
    print('YES!!! They are really love each other')
else:
    print('!!! They dont love at all !!!')
--------- Result ----------
YES!!! They are really love each other


'''
RegEx Functions :- 
--------------------
The re module offers a set of functions that allows us to search a string for a match.
'''

Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string

1) The findall() Function :- 
-------------------------------    
The findall() function returns a list containing all matches.

Ex :- 

import re

str1 = 'The rain in the Spain.'

x = re.findall('ai',str1)
y = re.findall('in',str1)

print(x)
print(y)
--------- Result ----------
['ai', 'ai']
['in', 'in', 'in']


NOTE :- The list contains the matches in the order they are found.

NOTE :- If no matches are found, an empty list is returned.

Ex :- 

import re

str1 = 'Rajesh loves Babudaya and Gududaya'

x = re.findall('daya',str1)
y = re.findall('Lover',str1)

print(x) # ['daya', 'daya']
print(y) # [] # Empty list .


2) The search() Function :- 
----------------------------    
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

Ex :- 

import re

str1 = "The rain in Spain"
str2 = 'Rajesh loves Usha'

x = re.search("\s", str1)
y = re.search("\s", str2)
print("The first white-space character is located in position:", x.start()) # 3
print("The first white-space character is located in position:", y.start()) # 6


NOTE :- If no matches are found, the value None is returned.

Ex :- 

import re

str1 = 'Rajesh Loves Babudaya'

x = re.search('Usha-girl',str1)
print(x) # None

3) The split() Function :- 
-----------------------------
The split() function returns a list where the string has been split at each match.

Ex :- Split at each white-space character.

import re

str1 = 'Rajesh and Usha both love each other and there is No Confusion at all.'

x = re.split('\s',str1)
print(x)
---------- Result --------
['Rajesh', 'and', 'Usha', 'both', 'love', 'each', 'other', 'and', 'there', 'is', 'No', 'Confusion', 'at', 'all.']


NOTE :- You can control the number of occurrences by specifying the maxsplit parameter.

Ex :- 

import re

str1 = 'Usha Means only Babudaya & Gududaya.'

x = re.split('\s',str1,1)

y = re.split('\s',str1,3)

print(x)
print(y)
---------- Result --------
['Usha', 'Means only Babudaya & Gududaya.']
['Usha', 'Means', 'only', 'Babudaya & Gududaya.']


4) The sub() Function :- 
---------------------------
The sub() function replaces the matches with the text of your choice.

Ex :- Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", " 9 ", txt)
print(x)
---------- Result --------
The 9 rain 9 in 9 Spain

Ex :- 

import re

str1 = 'Usha Means only Babudaya & Gududaya.'

x = re.sub('\s', ' LOVE ' , str1)
print(x)
---------- Result --------
Usha LOVE Means LOVE only LOVE Babudaya LOVE & LOVE Gududaya.

Ex :- 

import re

str1 = 'Rajesh Usha Rajesh'
x = re.sub('\s', ' LOVE ' , str1)
print(x)
---------- Result --------
Rajesh LOVE Usha LOVE Rajesh


NOTE :- You can control the number of replacements by specifying the count parameter.
 
Ex :- 

import re

str1 = 'Rajesh Usha Rajesh and They are so preety'
x = re.sub('\s', ' LOVE ' , str1 , 3)
print(x)
---------- Result --------
Rajesh LOVE Usha LOVE Rajesh LOVE and They are so preety


'''
Match Object :- 
----------------
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.
'''
Ex :- Do a search that will return a Match Object.

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # this will print an object

NOTE :- The Match object has properties and methods used to retrieve information about 
        the search, and the result.

1) span() returns a tuple containing the start-, and end positions of the match.
2) string returns the string passed into the function.
3) group() returns the part of the string where there was a match.
    
Ex :- 
Print the position (start- and end-position) of the first match occurrence.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) # (12, 17)


Ex :- Print the string passed into the function.

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) # The rain in Spain


Ex :- 

Print the part of the string where there was a match.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) # Spain
 
NOTE :- If there is no match, the value None will be returned, instead of the Match Object.

