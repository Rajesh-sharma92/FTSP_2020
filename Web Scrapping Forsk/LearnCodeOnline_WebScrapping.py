# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:19:49 2020

@author: Rajesh
"""

from bs4 import BeautifulSoup

import requests



response = requests.get('http://labs.forsk.in')

print(response)

soup = BeautifulSoup(response,"lxml")

print (soup)

print (soup.prettify())

print (soup.head)
print (soup.head.text)

print (soup.body)

print (soup.body.h1)
print (soup.body.h1.text)


print (soup.body.div)
print (soup.body.div.p)
print (soup.body.div.p.text)