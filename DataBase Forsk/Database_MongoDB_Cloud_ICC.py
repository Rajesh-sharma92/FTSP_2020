# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 22:29:41 2020

@author: Rajesh
"""

import pymongo
import pandas as pd 

cluster = pymongo.MongoClient('mongodb+srv://sharmarajesh:rs8217083006@cluster0-sudpb.mongodb.net/test?retryWrites=true&w=majority')

db = cluster['ICC_DB']
collection = db['ODI_coll']


def add_employee(idd, first, last, pay):
    unique_employee = collection.find_one({"id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        collection.insert_one(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Employee added successfully"


def fetch_all_employee():
    user = collection.find()
    for i in user:
        print (i)
   
     
df = pd.read_csv('E:/Web Scrapping Forsk/odi.csv')
records_= df.to_dict(orient='records')

results = collection.insert_many(records_)  

# collection.drop()      
        
        
        









