# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:45:38 2020

@author: Rajesh
"""
    #############################################################

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS


url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"

browser = webdriver.Chrome("E:\driver\chromedriver.exe")



browser.get(url)

sleep(2)

        #############################################################

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS1


url = "http://facebook.com"

browser = webdriver.Chrome("E:\driver\chromedriver.exe")

browser.get(url)

sleep(2)


