# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:45:36 2020

@author: Rajesh
"""
"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
"""

import requests

Amount = float(input('Enter Amount in USD :'))

url1 = "https://free.currencyconverterapi.com/api/v5/convert" # Base URL.

url2 = "?q=USD_INR&compact=ultra" # query string.

url3 = "&apiKey=07ca862e0b339dd56245" # API KEY.

url = url1+url2+url3

print(url)

response = requests.get(url)

jsondata = response.json()

print(jsondata)

total_value = Amount*(jsondata['USD_INR'])

print(total_value)


  ################# OR #################
  

import requests

Amount = float(input('Enter Amount in USD :'))

url = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=07ca862e0b339dd56245"

response = requests.get(url)

jsondata = response.json()

print(jsondata)

total_value = Amount*(jsondata['USD_INR'])

print(total_value)




















