# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:25:23 2020

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

"""
PICKLING CONCEPT in Machine Learning :- 
--------------------------------------
"""
# Here we will any trained Models & save into check the predicitions.

import pickle

with open('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\model_pickle','wb') as f:
    pickle.dump(regressor,f)
    
    
with open('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\model_pickle','rb') as f:
    mp = pickle.load(f)

mp.predict([[5000]]) # 859554.79452055

x = mp.predict([[1500]])  # 384297.94520548

----------------------------------------------------------------------------------------------------
"""
JOBLIB CONCEPT in Machine Learning :- 
--------------------------------------
"""
# This is also used like pickling concept but it is more useful when you have large number 
# numpy array data into datasets.

from sklearn.externals import joblib

joblib.dump(regressor,'E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\model_joblib')

mj = joblib.load('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\model_joblib')

mj.predict([[5000]]) # 859554

mj.predict([[1500]]) # 384297.94520548

# NOTE :- We just want to know what it contans the details the above file.

print(mj.coef_) # 135.78767123

print(mj.intercept_) # 180616.43835616

