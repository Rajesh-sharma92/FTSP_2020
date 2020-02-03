# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 08:45:42 2020

@author: Rajesh
"""

 ##  URL :- https://api.coindesk.com/v1/bpi/currentprice/<CODE>.json
 
import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
 
response = requests.get(url)
 
binfo = response.json()
 
print(type(binfo))
 
print(binfo)

print(binfo['time'])

print(binfo['time']['updated'])

print('Bitcoin Price as on',binfo['time']['updated'])

print(binfo['bpi']['USD']['rate'])
 
print('1 BitCoin = $', binfo['bpi']['USD']['rate'])
 
 
 
 