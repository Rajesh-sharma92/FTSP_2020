# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:30:25 2020

@author: Rajesh
"""

quarter = []
month = []
region = []
state = []
manager = []
salesperson = []
category = []
subcategory = []
quantity = []
unit_price = []
discount = []
sales = []

import random
import pandas as pd
quarter1 = [1,2,3,4,5]
month1 = ['January','February','March','April','may','june','july','august','September','October','November']
region1 = ['North','West','South','East']
manager1 = ['Anderson','Balley','Calley','Dame','Easen','Garrage','Hastings']
salesperson1 = ['Ashley','Blakely','Chandler','Denton','Adams','Childers','Dension','Azinger','Berkin','Celine','Deller']
category1 = ['Business','Casual']
Subcategory1 = ['Womens','Mens']
Quantity1 = [60,70,80,90,100,120,130,150,160,170,180,200]
unit_price1 = [5,6,7,8,9,10]

for i in range(1356):
    quarter.append(random.choice(quarter1))
    month.append(random.choice(month1))
    region.append(random.choice(region1))
    state.append('Minnesota')
    manager.append(random.choice(manager1))
    salesperson.append(random.choice(salesperson1))
    category.append(random.choice(category1))
    subcategory.append(random.choice(Subcategory1))
    quantity.append(random.choice(Quantity1))
    unit_price.append(random.choice(unit_price1))
    discount.append(5)
    sales.append(random.randrange(200, 1500, 20))
    
dict = {"Quarter":quarter,"Month":month,"Region":region,"State":state,"Manager":manager,"Salesperson":salesperson,
        "Category":category,"Subcategory":subcategory,"Quantity":quantity,
        "Unit Price":unit_price,"Discount":discount,"Sales":sales}    
    

# Convert into DatFrame to Excel sheets.
df = pd.DataFrame(dict)   

df.to_excel("E:/Power BI/Clothes_Sales.xlsx")
    
    
    
    
    
    
    