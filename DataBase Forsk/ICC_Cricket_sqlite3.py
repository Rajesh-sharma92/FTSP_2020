# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:01:59 2020

@author: Rajesh
"""
" ICC Cricket Sqlite3 "

import sqlite3
import pandas as pd

conn = sqlite3.connect('Icc_cricket.db')

data = conn.cursor()

data.execute("""create table ICC_Cricket(pos integer,
                                         Team text,
                                         Weighted Matches integer,
                                         Points integer,
                                         Rating integer
                                         )
                                      """)
conn.commit()




df = pd.read_csv('E:/Web Scrapping Forsk/odi.csv')
print(df)

df_exits = df.to_sql('ICC_Cricket',conn,if_exists='replace',index=False) # To store in data base.

read = data.execute('select * from ICC_Cricket') # To read data from DB.

read.fetchall()

data.execute('drop table ICC_Cricket')
conn.commit()









