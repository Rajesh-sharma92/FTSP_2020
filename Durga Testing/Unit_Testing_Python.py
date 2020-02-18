# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:41:36 2020

@author: Rajesh
"""
Testing :- 
-------
1) Unit Testing.
2) Integration Testing.

1) Unit Testing :- 
   ------------
   The process of testing whether a particular unit is working properly or not 
   is called unit Testing. It is also called as White box Testing.
   
Question (1) :- who is the responsible for unit testing ?
Answer :- Developers are responsible for unit testing in the industry.

Question (2) :- Have you ever involved in testing ?
Answer :- Yes, I have involved into it.

2) Integration Testing :- 
   -------------------
   The process of testing total / whole application (end-to-end) testing is called as Integration Testing.
   Means whether the whole application working fine or not ? It is also called as black box Testing.

Question (1) :- who is the responsible for Integration testing ? 
Answer :- QA Team (Quality Analysts) , Test engineers.
-----------------------------------------------------------------------------------------------------------
--> Test Scenarios
--> Test Cases
--> Test Suites

Gmail Application :-
-----------------
1) Testing login functionality.
2) Testing inbox functionality.

1) Testing login functionality :- Test Scenarios
   ---------------------------
   i) Valid username and Valid password. --> TC1
   i) Valid username  and Invalid password. --> TC2
   iii) Invalid username and Valid password. --> TC3
   iv) Invalid username and Invalid Password. --> TC4
   v) Empty username and Empty password. -->TC5
   vi) Valid username and Empty password. -->TC6
   vii) Empty username and valid password. -->TC7

NOTE :- The Test scenario contains multiple test cases.
NOTE :- Take all the test cases and put into a Test Suite and then each & every test 
cases will be executing. We will be knowing the like how many test cases are passed or failed.
---------------------------------------------------------------------------------------------

How to perfrom Unit Testing in Python :- 
-------------------------------------
module name : unittest (In-built python module and no need to install sepearately)
class name : TestCase 
Instance methods : 3 methods
1) setUp()
2) test()
3) tearDown()


class TestCaseDemo(TestCase):
--- > TestCaseDemo is the child class for TestCase.
-----------------------------------------------------------------------------------

import unittest
class TestCaseDemo(unittest.TestCase):
    
    def setUp(self):
        print('setUp method execution ......')
        
    # def test_method1(self): # test name is not fixed. we can take any method name but we need to test the prefix test.
    def test(self):    
        print('test method execution .....')
        # print(10/0) ZeroDivisionError: division by zero. Test Case = 'FAILED'
    
    def tearDown(self):
        print('tearDown method execution .....')
        
unittest.main()
------------------------------------------------------------------------------------
NOTE :- Can we declare 'N' no. of test cases methods.

import unittest
class TestCaseDemo(unittest.TestCase):
    
    def setUp(self):
        print('setUp method execution ......')
        
    def test_method1(self): 
        print('test method1 execution .....')
        
    def test_method2(self): 
        print('test method2 execution .....')
       # print(10/0)
            
    def tearDown(self):
        print('tearDown method execution .....')
        
unittest.main()

NOTE :- If we are using 'N' no. of test methods then we can see that test method 
will be executed like this.

setUp ---> test_method1 ---> tearDown 
setUp ---> test_method2 ---> tearDown 

NOTE :- setUp() & tearDown() are not changeable that means we can not modify their names.
setUp() & tearDown() both methods are fixed only in python.
-----------------------------------------------------------------------------------------
setUp() : open chrome browser 
test1() : test login functionality in google chrome.
tearDown() : close chrome browser

setUp() : open firefox browser 
test2() : test login functionality in firefox  chrome.
tearDown() : close firefox  browser
--------------------------------------------------------------------------------------
setUpClass(cls)

test1 : test login funcionality in chrome with valid username & valid password
test2 : test login funcionality in chrome with Invalid username & Invalid password

tearDownClass(cls)
--------------------------------------------------------------------------------------------
Examle :- If i have 10 test methods then how many these below methods are executing ?.

setUp() --------------- 10 times
tearDown() ------------- 10 times 
setUpClass() ----------- 1 time only (once only)
tearDownClass() -------- 1 time only (once only)
-------------------------------------------------------------------------------------
import unittest
class TestCaseDemo(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('SetUpClass method execution .....')
        
    def setUp(self):
        print('setUp method execution ......')
        
    def test_method1(self): 
        print('test method1 execution .....')
        
    def test_method2(self): 
        print('test method2 execution .....')
       # print(10/0)
            
    def tearDown(self):
        print('tearDown method execution .....')
        
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass method execution .....')
    
        
unittest.main()
-----------------------------------------------------------------------------------

import unittest
class TestCaseDemo(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('SetUpClass method execution .....')
        
    def setUp(self):
        print('setUp method execution ......')
        
    def test_method1(self): 
        print('test method1 execution .....')
        
    def test_method2(self): 
        print('test method2 execution .....')
        print(10/0)
       
    def test_method3(self): 
        print('test method1 execution .....')
        
    def test_method4(self): 
        print('test method2 execution .....')
        print(10/0)
            
    def tearDown(self):
        print('tearDown method execution .....')
        
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass method execution .....')
    
        
unittest.main()
--------------------------------------------------------------------------------------------
There are mainly 2 types of testing.

1) Manual Testing :- It performs by user / human itself step by step as per requirement.
   ---------------- 
2) Automation Testing :- We need to write the script in python and perform the same task 
   ------------------  without human involvement. It will be doing using selenium webdriver tool.
    
    Ex :- selenium , QTP , Load Runner 
    
------------------------------------------------------------------------------------------

import unittest
from selenium import webdriver
from time import sleep

class GoogleSerach(unittest.TestCase):
    
    def setUp(self):
        browser = webdriver.Chrome('E:\driver\chromedriver.exe')
        browser.get('https://youtube.com')
        browser.maximize_window()
        
    def test(self):
        print('The browser has opend successfully')
        print('WELCOME TO FORSK CODING SCHOOL')
        
    def tearDown(self):
        sleep(5)
        print('The browser has closed successfully')
        browser.close()
        
unittest.main()
-----------------------------------------------------------------------------------
Ex :- seleniumbymahesh.com

Testing login & logout functionality of HMS application :- 
-------------------------------------------------------
setUpClass() : To launch browser

test_login()
test_logout() 

tearDownClass() : To close browser
------------------------------------------------------------------------------
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep

class HMSLoginLogout(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('SetUpClass method Execution ...')
        global driver
        driver = webdriver.Chrome('E:\driver\chromedriver.exe')
        driver.get('http://seleniumbymahesh.com')
        driver.maximize_window()
        sleep(10)
        
    def test_login(self):
        print('test_login method execution ...')
        driver.find_element_by_xpath('/html/body/div/header/div[2]/div/div/div[2]/div/div[2]/div/ul/li[7]/a').click()
        driver.find_element(By.NAME,'username').send_keys('admin')
        driver.find_element(By.NAME,'password').send_keys('admin')
        driver.find_element(By.NAME,'submit').click()
        sleep(10)
        
    def test_logout(self):
         print('test_logout method execution ...')
         driver.find_element_by_xpath('/html/body/div[2]/div/h3/a').click()
         
        
    @classmethod
    def tearDownClass(cls):
         print('tearDownClass method Execution ...')
         sleep(10)
         driver.quit()
         
unittest.main()

*******************  Result ***********************

unittest.main()
SetUpClass method Execution ...
test_login method execution ...
.test_logout method execution ...
.tearDownClass method Execution ...

----------------------------------------------------------------------
Ran 2 tests in 49.891s

OK

NOTE :- OK means 2 test cases were success without any issue.













 
         
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    









































































    
    
    
    




































































































        
        
        










    
        






























   