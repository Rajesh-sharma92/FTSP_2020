# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:40:30 2020

@author: Rajesh
"""

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""

from bs4 import BeautifulSoup 
import requests

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/test'

response = requests.get(url).text
print(response)


soup = BeautifulSoup(response , 'lxml')
print(soup)

T20 = soup.find('table',class_='table')
print(T20)

A = []
B = []
C = []
D = []
E = []

for row in T20.findAll('tr'):
   cells = row.findAll('td')
   
   if len(cells)!=0:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        
from collections import OrderedDict
col_name = ['Pos','Team','Weighted Matches','Points','Rating']
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
print(col_data)

import pandas as pd
df = pd.DataFrame(col_data)
df.to_csv('E:/Web Scrapping Forsk/Test.csv')

