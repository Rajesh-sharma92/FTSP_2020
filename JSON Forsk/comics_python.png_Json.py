# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:00:06 2020

@author: Rajesh
"""
 
"""
Code Challenge

Download the image from the URL and store in a file

https://imgs.xkcd.com/comics/python.png

"""

import requests

response = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('E:/JSON Forsk/python.png','wb') as f:
    
    f.write(response.content)
    
       
 ######### OR ##############    
    
  
import requests

response = requests.get('https://i.udemycdn.com/course/750x422/385462_34ce.jpg')

with open('E:/JSON Forsk/Udemy.png','wb') as f:
    
    f.write(response.content)
    
  ############# OR ##############


import requests

response = requests.get('https://i.pinimg.com/originals/58/f4/72/58f4723d8f23906bdcb058604075ad2a.png')

with open('E:/JSON Forsk/Facebook.png','wb') as f:
    
    f.write(response.content)
    
    
      
    
    
    
    
    
    
    
    
