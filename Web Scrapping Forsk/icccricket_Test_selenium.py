# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:47:02 2020

@author: Rajesh
"""

from selenium import webdriver
from time import sleep

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings'

browser = webdriver.Chrome('E:\driver\chromedriver.exe')

#browser.maximize_window()

browser.get(url)

print('The browser has opend successfully')

sleep(2)

Test = browser.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div[1]/ul/li[1]/a')
Test.click() 


test = browser.find_element_by_class_name('table')

print(test)

A = []
B = []
C = []
D = []
E = []

for row in test.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    if len(cells) == 5:

        # if len(cells)!= 0:
        
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
df=pd.DataFrame(col_data)
df.to_csv('E:/Web Scrapping Forsk/Test_selenium.csv')

print('The browser has closed successfully')

sleep(2)

browser.quit()
