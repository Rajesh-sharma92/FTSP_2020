# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:49:18 2020

@author: Rajesh
"""

from selenium import webdriver
from time import sleep

url = 'https://youtube.com'

browser = webdriver.Chrome('E:\driver\chromedriver.exe')

browser.get(url)

#browser.maximize_window()

sleep(2)

print('The browser has opend successfully')

search = browser.find_element_by_id('search')

search.send_keys('forsk coding school')

sleep(2)

search_button = browser.find_element_by_id('search-icon-legacy')

search_button.click()

sleep(5)

channel = browser.find_element_by_id('channel-title')

channel.click()

sleep(5)

subscribe_button = browser.find_element_by_xpath('//*[@id="buttons"]')

sleep(5)

subscribe_button.click()

sleep(5)

print('The browser has closed successfully')

browser.quit()




