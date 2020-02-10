# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:31:27 2020

@author: Rajesh
"""
"""
Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
import sqlite3
from pandas import DataFrame

conn = sqlite3.connect('db_University.db')

c = conn.cursor()
conn.commit()
c.execute('DROP TABLE db_University')
c.execute("""create table db_University(
        Student_Name text,
        Student_Age integer,
        Student_Roll_no integer,
        Student_Branch text
        )
         """)
conn.commit()

c.execute("INSERT INTO db_University VALUES('Rajesh', 25,1001,'CSE')")
c.execute("INSERT INTO db_University VALUES('Ravi', 30,1002,'EEE')")
c.execute("INSERT INTO db_University VALUES('Gandhi', 35,1002,'Civil')")
c.execute("INSERT INTO db_University VALUES('Rahul', 45,1004,'Arch')")
c.execute("INSERT INTO db_University VALUES('Kamesh', 55,1005,'CS-IT')")

conn.commit()

c.execute('select * from db_University')

print(c.fetchone())

print(c.fetchmany(2))

print(c.fetchall())

c.execute("SELECT * FROM db_University")

df = DataFrame(c.fetchall())
df.columns = ('Student_Name','Student_Age','Student_Roll_no','Student_Branch')
conn.close()

#  print(c.fetchone())




























