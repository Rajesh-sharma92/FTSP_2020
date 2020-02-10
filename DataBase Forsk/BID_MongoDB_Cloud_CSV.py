# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:49:22 2020

@author: Rajesh
"""
"""
Code Challenge 3
In the Bid plus Code Challenege =
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database MongoDB on cloud.
"""

import pymongo
import pandas as pd 

cluster = pymongo.MongoClient('mongodb+srv://sharmarajesh:rs8217083006@cluster0-sudpb.mongodb.net/test?retryWrites=true&w=majority')

db = cluster['Zem_Details']
collection = db['BID_Details']

df = pd.read_csv('E:/Web Scrapping Forsk/bidplus.csv')
records_= df.to_dict(orient='records')

results = collection.insert_many(records_)  

