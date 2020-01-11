# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:53:34 2020

@author: Rajesh
"""

Today_Temp=int(input("Enter the Today temperature of City :"))
far_temp=((Today_Temp*(9/5))+32)
kel_temp=(Today_Temp+273)
print("**************************************")
print("Temperature of the City :", Today_Temp)
print("Temperature in Farenheit :", far_temp)
print("Temperature in Kelvin :", kel_temp)