# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:32:28 2020

@author: Rajesh
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "https://bidplus.gem.gov.in/bidlists?bidlists&page_no=1"
browser = webdriver.Chrome("E:/driver/chromedriver.exe")  ## open chrome browser
print('The browser has opened successfully')
browser.get(url)  ## hit the given url
sleep(2)          ## delay

#Generate lists
A=[]   ## bid no.
B=[]   ## department
C=[]   ## item
D=[]   ## quantity
E=[]   ## start date
F=[]   ## end date

i=0
while(i<5):
    
    page = browser.find_element_by_id("pagi_content")  
    for row in page.find_elements_by_class_name("border"):
        
        header= row.find_element_by_tag_name("a")  ## bid no.
        dep= row.find_element_by_class_name("add-height")  ## department
        item= row.find_elements_by_tag_name("span")   ## item,quantity,start,end
        
        A.append(header.text.strip())
        B.append(dep.text.strip())
        C.append(item[0].text.strip())
        D.append(item[1].text.strip())
        E.append(item[2].text.strip())
        F.append(item[3].text.strip())
        
    next_page= browser.find_element_by_xpath('/html/body/section[2]/div/div/div/div[3]/ul/li/ul/li[5]/a').click()
    sleep(1)
    i=i+1

print('The browser has closed successfully')
browser.quit()

import pandas as pd
from collections import OrderedDict

col_name= ['BID NO','items','Quantity Required','Department Name And Address','Start Date','End Date']
col_data = OrderedDict(zip(col_name,[A,C,D,B,E,F]))

df = pd.DataFrame(col_data) 
df.to_csv("bidplus.csv")













browser.quit()



















