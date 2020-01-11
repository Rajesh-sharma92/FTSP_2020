# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:49:39 2020

@author: Rajesh
"""
User_wgt=int(input("Enter the weight of user in kgs:"))
User_Height=(float(input("Enter the User Total Height :")))
one_foot=(0.3048)
ft_mtrs_Convert=(float(one_foot*User_Height))
Res=(User_wgt/ft_mtrs_Convert)
BMI=(Res/ft_mtrs_Convert)
print("The Height in cms : ", ft_mtrs_Convert)
print("The Division of Weight and Height :", Res)
print("The BMI Value :", BMI)





