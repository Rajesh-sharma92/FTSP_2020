# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:40:42 2020

@author: Rajesh
"""

ofc_travel=float(input("Enter the travel distance to office :"))
fuel_Cost=float(input("Enter the fuel cost per Litre :"))
Vehical_Fuel_avg=float(input("Enter the Vehicle Fuel average :"))
Per_day_fuel_Used=float(ofc_travel/Vehical_Fuel_avg)
Per_day_Cost_ofc=float(fuel_Cost*Per_day_fuel_Used)
print("************************************")
print("Total Travalled distance per day to office :", ofc_travel)
print("Total cost of fuel per day :", fuel_Cost)
print("The Per day total fuel used :", Per_day_fuel_Used)
print("The Per day total cost to office :", Per_day_Cost_ofc)
