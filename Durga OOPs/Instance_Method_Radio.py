# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:08:47 2020

@author: Rajesh
"""
class Radio_station:
    def __init__(self,st_name,st_frequency):
        self.st_name = st_name
        self.st_frequency = st_frequency
        
    def channel_Name(self):
        print('Station_Name :',self.st_name)
        print('Station_Frequency :', self.st_frequency)
        
    def Channel_Frequency(self):
        if self.st_frequency == 93.5:
            print('Red FM')
        elif self.st_frequency == 94.5:
            print('Radio Mirchi')
        elif self.st_frequency == 95.0:
            print('Red FM Famous from Jaipur')
        else:
            print('This channel no. is not Available in Radio')
           
         
n = int(input('Enter your favioriate channels :'))
for i in range(n):
    
    st_name = input('Pls enter the channel name :')
    st_frequency = float(input('pls enter the channel number :'))
    
    r = Radio_station(st_name,st_frequency)
    r.channel_Name()  
    r.Channel_Frequency()
    print('*'*20)
    
            
        
