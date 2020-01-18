# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:59:32 2020

@author: Rajesh
"""

User_wgt=int(input('\u0905\u092A\u0928\u0940' '\u090A\u0945\u0902\u091A\u093E\u0908' '\u0926\u0930\u94D\u091C' '\u0915\u0930\u0910'))
User_Height=(float(input("Enter the User Total Height :")))
one_foot=(0.3048)
ft_mtrs_Convert=(float(one_foot*User_Height))
Res=(User_wgt/ft_mtrs_Convert)
BMI=(Res/ft_mtrs_Convert)

print('')

print("The Height in cms : ", ft_mtrs_Convert)
print("The Division of Weight and Height :", Res)
print("The BMI Value :", BMI)


