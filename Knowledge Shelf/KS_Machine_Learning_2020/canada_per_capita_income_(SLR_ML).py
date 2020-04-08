# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:21:38 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\canada_per_capita_income.csv')
dataset.head()
*************
  year  per capita income (US$)
0  1970              3399.299037
1  1971              3768.297935
2  1972              4251.175484
3  1973              4804.463248
4  1974              5576.514583

features = dataset.iloc[:,:1].values
labels = dataset.iloc[:,[1]].values

plt.scatter(features,labels,color='Blue')
plt.xlabel('Years')
plt.ylabel('Incomes(U$)')
plt.title('Per Capital Income Pridiction Graph')
#plt.savefig('path')
plt.show()

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

x = regressor.predict([[2020]])
x[0] # 41288.69409442

x = regressor.predict([[2030]]) # 49573.34484664

x = regressor.predict([[2050]]) # 66142.6463511


