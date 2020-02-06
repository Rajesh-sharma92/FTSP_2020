# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:05:50 2020

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

#sleep(2)

search = browser.find_element_by_id('search')

search.send_keys('durgasoft solutions')

sleep(5)

search_button = browser.find_element_by_id('search-icon-legacy')

search_button.click()

sleep(5)

print('The browser has closed successfully')

browser.quit()


