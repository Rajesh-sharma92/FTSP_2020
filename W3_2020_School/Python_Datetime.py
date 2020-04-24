# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:24:01 2020

@author: Rajesh
"""
'''
Python Datetime :- 
---------------------
'''
Python Dates :- 
----------------
A date in Python is not a data type of its own, but we can import a module named datetime
to work with dates as date objects.

NOTE :- Import the datetime module and display the current date.

Ex :- 

import datetime

x = datetime.datetime.now()

print('The Current date & time of system :' ,x)
--------- Result ---------
The Current date & time of system : 2020-04-24 12:28:37.812703

NOTE :- The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Ex :- Return the year and name of weekday.

import datetime

x = datetime.datetime.now()

print('The Current Year Running :', x.year)

print('The Current Week Day Name :', x.strftime('%A'))

print('The Type Of x :', type(x))

----------- Result --------
The Current Year Running : 2020
The Current Week Day Name : Friday
The Type Of x : <class 'datetime.datetime'>

'''
Creating Date Objects :- 
----------------------------
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.
'''
Ex :- How to create a Date Object.

import datetime

x = datetime.datetime(2020,5,3)

print('Date & Time are :', x)
----------- Result --------
Date & Time are : 2020-05-03 00:00:00


NOTE :- The datetime() class also takes parameters for time and timezone 
(hour, minute, second, microsecond, tzone), but they are optional, and has a 
default value of 0, (None for timezone).

Ex :- 
x = datetime.datetime(2020,5,3,12,55,30)
print(x) # 2020-05-03 12:55:30


'''
The strftime() Method :- 
--------------------------
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.
'''
Ex :- Display the name of the Current month.

import datetime

x = datetime.datetime.now()

print('The Month of current Date & Time :', x.strftime('%B'))
----------- Result --------
The Month of current Date & Time : April

Ex :- Display the name of the Previous 2 months.

import datetime

x = datetime.datetime(2020,2,29)

print('The Month of current Date & Time :', x.strftime('%B'))
----------- Result --------
The Month of current Date & Time : February

Directive	Description	Example	Try it
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%

NOTE :- There so many other methods to get the details about Date & Time related.

Ex :- 

import datetime

x = datetime.datetime.now()

print('The Week day Name Short Form :', x.strftime('%a'))
# The Week day Name Short Form : Fri

print('The Week day Name Full Form :', x.strftime('%A'))
# The Week day Name Full Form : Friday

print('Weekday as a number 0-6 :', x.strftime('%w')) # 5


print('Day of month:', x.strftime('%d')) # 24

print('Month name, short version:', x.strftime('%b')) # 24
# Month name, short version: Apr

print('Month name, Full version:', x.strftime('%B')) # 24
# Month name, full version: April

print('Year, short version, without century :', x.strftime('%y')) # 04
# Year, short version, without century : 20

print('Year, full version :', x.strftime('%Y')) 
# Year, full version : 2020

print('Current 24-Hours format :', x.strftime('%H')) # Current Hour : 14

print('Current 12-Hours format :', x.strftime('%I')) # Current Hour : 02

print('AM / PM Details :', x.strftime('%p')) # PM

print('Minutes :', x.strftime('%M')) # Minutes : 37

print('Seconds :', x.strftime('%S')) # Seconds : 12

print('Microsecond :', x.strftime('%f')) # Microsecond : 279493

print('UTC offset	+0100:', x.strftime('%z')) # UTC offset      +0100:

print('Timezone    CST   :', x.strftime('%Z')) # Timezone    CST     

print('Day number of year :', x.strftime('%j')) # Day number of year : 115

print('Week number of year, Sunday as the first day of week, 00-53	52 :', x.strftime('%U')) 
# Week number of year, Sunday as the first day of week, 00-53     52 : 16

print('Week number of year, Monday as the first day of week, 00-53	52 :', x.strftime('%W')) 
# Week number of year, Monday as the first day of week, 00-53     52 : 16

print('Local version of date and time :', x.strftime('%c')) 
# Local version of date and time : Fri Apr 24 14:37:12 2020

print('Local version of date :', x.strftime('%x')) 
# Local version of date : 04/24/20

print('Local version of Time :', x.strftime('%X')) 
# Local version of Time : 14:37:12

print('A % character :', x.strftime('%%'))  # A % character : %


