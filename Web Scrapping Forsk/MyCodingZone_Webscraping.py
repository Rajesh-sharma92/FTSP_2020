# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 07:37:25 2020

@author: Rajesh
"""

from bs4 import BeautifulSoup

import requests

response = requests.get('https://www.mycodingzone.net/blog/english').text

print(response)

soup = BeautifulSoup(response,'lxml')

print(soup)

print(soup.prettify())

for para in soup.find('p'): # find() function provides the first paragraph.
    print(para)

for para in soup.find_all('p'): # find_all() function provides the all available  paragraph.
    print(para)

for para in soup.find_all('p'):
    print(para.text)
    
for a in soup.find_all('a'):
    print(a.text)    
    
for links in soup.find_all('a'):
    link = links.get('href')
    print(link)
  
    # It is for all available links in this particular page.
    
for links in soup.find_all('a'):
    link = links.get('href')
    if link[0:3] == '../' and link!= '#':
        print('https://www.mycodingzone.net' + link[2:len(link)])
    elif link[0] == '/' and link!= '#':
         print('https://www.mycodingzone.net' + link)
    elif link!= '#':
         print(link)
         
         
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    