# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:54:15 2020

@author: Rajesh
"""

User_Height=(float(input("Enter the User Total Height :")))
one_foot=(0.3048)
one_inch=(0.0254)
one_mtr=(100)
ft_mtrs_Convert=(float(one_foot*User_Height))
print("User Height in the Foot is :" , ft_mtrs_Convert)


User_Inch_Hgt=(float(input("Enter the User Height in Inches :")))
Inch_mtrs_Convert=float((one_inch*User_Inch_Hgt))
print("User Height in the Metre is :" , Inch_mtrs_Convert)

print("Total Height in Meters are :", (ft_mtrs_Convert+Inch_mtrs_Convert))
print("Total Height in Centimeters are :", (100*(ft_mtrs_Convert+Inch_mtrs_Convert)))



