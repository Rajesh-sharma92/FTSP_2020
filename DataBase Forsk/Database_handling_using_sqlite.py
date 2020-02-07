# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 08:37:29 2020

@author: Rajesh
"""
"""
Database handling using sqlite 
"""

import sqlite3
from pandas import DataFrame

# File based database ( connects if exists or creates a new one if it does not exists ) 
conn = sqlite3.connect('employee.db')

# creating cursor
c = conn.cursor()


#Delete the table
c.execute('DROP TABLE employees')
conn.commit()

# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""create table employees(
        id integer,
        first text,
        last text,
        pay integer
    )"""
)

conn.commit()

# STEP 2
c.execute("INSERT INTO employees VALUES(10,'Rajesh','sharma',25000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Rohit', 'Mishra', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")

c.execute("insert into employees values(50,'Ramu', 'Shekhawat', 30000)")

conn.commit()

# STEP 3
c.execute("SELECT * FROM employees")
#c.execute('SELECT * FROM employees')
#"SELECT * FROM employees WHERE last = 'Fernandes' "

# STEP 4
# returns one or otherwise None as a tuple
print(c.fetchone())

# returns one or otherwise None as a tuple
print(c.fetchmany(3))

# returns a list of tuples
print(c.fetchall())

# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")

# STEP 5
df = DataFrame(c.fetchall()) # putting the result into Dataframe
df.columns = ['id','first','last','pay']

# df.to_csv("E:\DataBase Forsk\employee.csv")

# STEP 6
# closing the connection 
conn.close()

print(c.fetchone())









































