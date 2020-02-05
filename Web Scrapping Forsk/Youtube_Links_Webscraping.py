# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:26:42 2020

@author: Rajesh
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com/watch?v=VQQ6uiXDlGo&list=PL47S5PRS_XOd7p4svEN75YR45eARHXdqQ&index=2&pbjreload=10'
response = requests.get(url).text
print(response)

soup = BeautifulSoup(response , 'lxml')
print(soup)

for links in soup.find_all('a'):
    link = links.get('href')
    if link[0:3] == '/wa':
        print('https://www.youtube.com' + link)
        
        
########################################################################

from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com/results?search_query=durgasoft+python'
response = requests.get(url).text
print(response)

soup = BeautifulSoup(response , 'lxml')
print(soup)

for links in soup.find_all('a'):
    link = links.get('href')
    if link[0:3] == '/wa':
        print('https://www.youtube.com' + link)
        
        
        
        
    

        