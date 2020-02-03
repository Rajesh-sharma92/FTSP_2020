# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 18:27:33 2020

@author: Rajesh 
"""

"""
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your working diretory with the same
name as the image name.

Do not hardcode the name of the image

"""
import requests

response = requests.get('http://forsk.in/images/Forsk_logo_bw.png') # Response means Header + data.

with open('E:/JSON Forsk/abc.jpg','wb') as f:
    
    f.write(response.content)
    
       
   ##############  OR ##############



import requests

response = requests.get('https://cdn.motor1.com/images/mgl/Bo0Qj/s3/2021-new-lead.jpg')

with open('E:/JSON Forsk/abc.jpg','wb') as f:
    
    f.write(response.content)
    
       