# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:28:40 2020

@author: Rajesh
"""

pr_age=int(input("Enter the present Age of the user :"))
max_hrate=(220-pr_age)
Lowerend_hrate=((max_hrate*70)/100)
Higherend_hrate=((max_hrate*85)/100)
print("The Maximum Heart Rate :",max_hrate)
print("The Lowerend Heart Rate is :", Lowerend_hrate)
print("The Higher Heart Rate is :", Higherend_hrate)