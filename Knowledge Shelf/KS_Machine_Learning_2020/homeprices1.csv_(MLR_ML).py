# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:58:45 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\homeprices1.csv')
dataset.head()
****************
   area  bedrooms  age   price
0  2600       3.0   20  550000
1  3000       4.0   15  565000
2  3200       NaN   18  610000
3  3600       3.0   30  595000
4  4000       5.0    8  760000

# To check the Nan values into dataset.
dataset.isnull().any(axis=0) # We have Nan Values into Bedrooms column.
*********
area        False
bedrooms     True
age         False
price       False

bedrooms_median = dataset['bedrooms'].median() # 4.0

# Now fill the Nan values into dataset.
dataset['bedrooms'].fillna(bedrooms_median ,inplace = True)
dataset.head()
***********
  area  bedrooms  age   price
0  2600       3.0   20  550000
1  3000       4.0   15  565000
2  3200       4.0   18  610000
3  3600       3.0   30  595000
4  4000       5.0    8  760000

features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,[-1]].values


# Now we will train/fitting of the model.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

print(regressor.coef_) # [[  112.06244194 23388.88007794 -3231.71790863]]
print(regressor.intercept_) # 221323.0018654

# Now we will do the predicition as per the Questions asked.
regressor.predict([[3000,3,40]]) # 498408.25158031

# y = m1x1 + m2x2 + m3x3 + c

y = ((112.06244194*3000+23388.88007794*3+(-3231.71790863*40))+221323.0018654)
print(y) # 498408.25157402

x = regressor.predict([[2500,4,5]])
print(x[0]) # 578876.03748933



 




