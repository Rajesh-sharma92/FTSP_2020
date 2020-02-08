# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 16:30:22 2020

@author: Rajesh
"""
"""
Database handling using MySQL on Cloud
Relational DB Vs NoSQL DB
"""
"""
https://www.db4free.net
https://www.db4free.net/phpMyAdmin/
MySQL Host Name : db4free.net
Port : 3306
MySQL database name:  rajesh_forsk
MySQL username: sharma_forsk
MySQL user password: forsk@#2020
Email address:  sharma90126@gmail.com
MYSQL URL : mysql://forsk_root:cooler2112@db4free.net/forsk_test

"""

# !pip install mysql-connector-python

import mysql.connector
# connect to  MySQL server along with Database name.
conn = mysql.connector.connect(user='rajesh_forsk',password='forsk9036',
                               host='db4free.net',database='sharma_forsk')

data = conn.cursor()

data.execute ("""CREATE TABLE Test(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")

conn.commit()

data.execute("INSERT INTO Test VALUES (01,'Sylvester', 'Fernandes', 50000)")
data.execute("INSERT INTO  Test VALUES (02,'Yogendra', 'Singh', 70000)")
data.execute("INSERT INTO Test VALUES (03,'Rohit', 'Mishra', 30000)")
data.execute("INSERT INTO Test VALUES (04,'Kunal', 'Vaid', 30000)")
data.execute("INSERT INTO Test VALUES (05,'Devendra', 'Shekhawat', 30000)")

#data.execute('drop table test')

data.execute('select * from Test')
conn.commit()

print(data.fetchone())
print(data.fetchmany(2))
print(data.fetchall())

data.execute("SELECT * FROM Test")

df = DataFrame(data.fetchall())

df.columns = ['id','first','last','pay']

print(df)

conn.close()






















