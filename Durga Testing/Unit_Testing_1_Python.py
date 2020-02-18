# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:00:49 2020

@author: Rajesh
"""
Unit Testing :-
------------
unittest ---> module
TestCase  ----> class

There are some functions as below :- 
---------------------------------
setUp()
test()
tearDown()

setUpClass()
tearDownClass()

NOTE :- for every test method setUp() & tearDown() functions will be executed.
NOTE :- for All test methods both methods like setUpClass() & tearDownClass() will be executed only once.

selenium : Package
webdriver : module

webdriver module contains several functions & classes to test functionality
of the web application.

launch Browser :- 
--------------
Browser driver must be required which is responsible to launch our browser.

for selenium website :- seleniumhq.org

Install selenium :- pip install selenium
------------------------------------------------------------------------------------------------
Question (1) :- How to launch a any browser by using selenium ?
Answer :- There are some of the steps to launch browser.

from selenium import webdriver
driver = webdriver.Chrome('E:/driver/chromedriver.exe')

from selenium import webdriver
driver = webdriver.Firefox('E:/driver/geckodriver.exe')
--------------------------------------------------------------------------------------------
browser Interaction & Navigation of webpages :- 
--------------------------------------------
driver = webdriver.Chrome('E:/driver/chromedriver.exe')
1) driver.get(url)

# It is used for open specified url.
 
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('E:/driver/chromedriver.exe')
driver.get('https://www.facebook.com')
# To Maximize window.
driver.maximize_window()
sleep(5)
#driver.minimize_window()

print('The Title of Page : ', driver.title)
print('The current URL of the Page :', driver.current_url)
sleep(5)
print('Pls Refresh the current Page :', driver.refresh)
sleep(5)
driver.get('http://www.durgasoft.com')
driver.maximize_window()
print('The Title of Page : ', driver.title)
print('The current URL of the Page :', driver.current_url)
driver.back()
print('After back current url :', driver.current_url)
driver.forward()
print('After forward current url :', driver.current_url)
sleep(5)
driver.close() # To close the current window.

# driver.quit() # To close the associated window.
------------------------------------------------------------------------------------------
How to locate web elements :- 
--------------------------
Web elements :- Anything presents on webpage are called as webelement.
------------
driver.find_element_by_id('id')
driver.find_element_by_name('name')
driver.find_element_by_xpath('xpath')
driver.find_element_by_css_selector('css selector')
driver.find_element_by_link_text('link text')
driver.find_element_by_tag_name('tag')

driver.find_element(By.ID,'id')
driver.find_element(By.NAME,'name')
-----------------------------------------------------------------------------------------------
from selenium import webdriver
import unittest
from time import sleep

class GoogleSearchDemo(unittest.TestCase):
    
    def setUp(self):
        global driver
        driver = webdriver.Chrome('E:/driver/chromedriver.exe')
        driver.get('https://google.com')
        print('Browser has opened successfully')
        #driver.maximize_window()
        
    def test(self):
        driver.find_element_by_name('q').send_keys('Mahesh Babu')
        driver.find_element_by_name('btnK').click()
        driver.find_element_by_class_name('LC201b').click()
        sleep(10)
        
    def treaDown(self):
        print('Browser has closed successfully')
        driver.close()

unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    










































































