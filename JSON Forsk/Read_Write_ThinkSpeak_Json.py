# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:27:02 2020

@author: Rajesh
"""

import requests


write_data = requests.get("https://api.thingspeak.com/update?api_key=5ADK21T8TA87X5PN&field1=590&field2=9900")

Read_data = requests.get("https://api.thingspeak.com/channels/979935/feeds.json?api_key=9HM7WEZ4MH4VV689&results=2")

x = Read_data.json()

print(x)


 ################# OR ####################
 

import requests
field1=input("Enter the value:")
field2=input("Enter the value:")

write_data = requests.get("https://api.thingspeak.com/update?api_key=5ADK21T8TA87X5PN&field1=500&field2=900")

Read_data = requests.get("https://api.thingspeak.com/channels/979935/feeds.json?api_key=9HM7WEZ4MH4VV689&results=2")

x = Read_data.json()

print(x)

print(x["channel"]['name'])
print(x["channel"]['id'])
print(x['feeds'])
print(x['feeds']['created_at'])








