# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:32:49 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\homeprices.csv')
dataset.head()
*********
   area   price
0  2600  550000
1  3000  565000
2  3200  610000
3  3600  680000
4  4000  725000

features = dataset.iloc[:,:1].values
labels = dataset.iloc[:,[1]].values

plt.scatter(features,labels,color='Blue')
plt.xlabel('Area (Sqft)')
plt.ylabel('Price (U$)')
plt.title('New House Price Pridiction Graph')
#plt.savefig('path')
plt.show()

# Now we will apply the SLR algorithm.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

# Now we will predict the Area = 3300 & what will be the price of new House ?
x = regressor.predict([[3300]])
x[0] # 628715.75342466

# We know that straight Line Equation 
# y = mx+c
 # where m = slope , c = Intercept.
 
print('The Slope(m) :', regressor.coef_) # The Slope(m) : [[135.78767123]]
print('The Intercept(c) :', regressor.intercept_) # The Intercept(c) : [180616.43835616]

y = (135.78767123*3300)+(180616.43835616)
print(y) # 628715.75341516

# Now we will predict the Area = 5000 & what will be the price of new House ?
x = regressor.predict([[5000]]) # [859554.79452055

-----------------------------------------------------------------------------------------------
dataset = pd.read_csv(r'E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\areas.csv')
dataset.head()
*******
  area
0  1000
1  1500
2  2300
3  3540
4  4120

p = regressor.predict(dataset)

# Now we will add new column to dataset like Prices.

dataset['Prices'] = p
dataset.head()
************
  area         Prices
0  1000  316404.109589
1  1500  384297.945205
2  2300  492928.082192
3  3540  661304.794521
4  4120  740061.643836

dataset.to_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\Price_Predictions.csv' , index = False)
print(dataset) # Here index = False Means earlier it was giving the Default Index also bit now it will remove it.

# Now we will plot the graph.

features = dataset.iloc[:,:1].values
labels = dataset.iloc[:,[1]].values

plt.scatter(features,labels,color='Blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('New House Price Pridiction Graph')
plt.plot(features,regressor.predict(features),color='Red')
#plt.savefig('path')
plt.show()















