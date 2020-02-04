# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:25:47 2020

@author: Rajesh
"""

import requests

from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/'

r = requests.get(url)

soup = BeautifulSoup(r.content)

print(soup.prettify())

