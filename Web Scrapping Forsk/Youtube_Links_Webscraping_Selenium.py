# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 07:38:44 2020

@author: Rajesh
"""

from selenium import webdriver
from time import sleep
# from bs4 import BeautifulSoup as BS

url = 'https://www.youtube.com'

browser = webdriver.Chrome('E:\driver\chromedriver.exe')

browser.get(url)

sleep(2)

print('The browser has opend successfully')

sleep(10)

print('The browser has closed successfully')

browser.quit()

     














