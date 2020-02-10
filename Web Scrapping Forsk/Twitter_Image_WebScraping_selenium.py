# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:36:03 2020

@author: Rajesh
"""

from selenium import webdriver
from time import sleep

url = 'https://twitter.com'
browser = webdriver.Chrome('E:\driver\chromedriver.exe')
browser.maximize_window()
browser.get(url)
print('Browser has opened successfully')

sleep(2)

Log_In = browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/a[2]/div')
Log_In.click()
sleep(2)
User_name = browser.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input')
User_name.send_keys('Rajeshs86251602')
sleep(2)
Password = browser.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input')
Password.send_keys('Marwadi@#2020')
sleep(2)
LogIn_Button = browser.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
LogIn_Button.click()
print(' !! Twitter is very famous on social Media !! ')
sleep(5)
print('Browser has closed successfully')
browser.quit()


