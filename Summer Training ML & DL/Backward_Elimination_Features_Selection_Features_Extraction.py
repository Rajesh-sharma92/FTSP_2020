# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:02:35 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Salary_Classification.csv')

dataset.head()
****************
    Department  WorkedHours  Certification  YearsExperience  Salary
0  Development         2300              0              1.1   39343
1      Testing         2100              1              1.3   46205
2  Development         2104              2              1.5   37731
3           UX         1200              1              2.0   43525
4      Testing         1254              2              2.2   39891

features = dataset.iloc[:,:-1].values

labels = dataset.iloc[:,-1].values

# Encoding Categorial columns data.
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

columnTransformer = ColumnTransformer([('encoder',OneHotEncoder(),[0])] , remainder = 'passthrough')
features = np.array(columnTransformer.fit_transform(features) ,dtype = np.float32)

# Avoiding the Dummy Variable Trap
# Dropping the first columan

features = features[:,1:]
print(features)


# Now we will be applying the Stats Model like Linear Regression only. 
# OLS Means Optimal Least Square method or Linear Regression both are same only.

import statsmodels.api as sm

# Add the Constant column to dataset.
features = sm.add_constant(features)
print(features)

# Now we will do the Copy of the Original features data & we perform the OLS on that itself.

features_opt = features[:,[0,1,2,3,4,5]]

regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()

regressor_OLS.summary() # Here we have the x2 has the highest p value and we need to remove it.


features_opt = features[:,[0,1,3,4,5]] # x2 remove from features_opt

regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()

regressor_OLS.summary() 


features_opt = features[:,[0,1,3,5]] # x3 means Certification Column  remove from features_opt

regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()

regressor_OLS.summary() 


features_opt = features[:,[0,3,5]] # x4 means WorkedHours  Column  remove from features_opt

regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()

regressor_OLS.summary() 


features_opt = features[:,[0,5]] # x1 means Dummy variable1  Column  remove from features_opt

regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()

regressor_OLS.summary() 


# Add these code to Automatic Removes p values from the Dataset.
import statsmodels.api as sm
import numpy as np

features_obj = features[:,[0,1,2,3,4]]
features_obj = sm.add_constant(features_obj)

while(True):
    regressor_OLS = sm.OLS(endog=labels,exog=features).fit()
    pvalues = regressor_OLS.pvalues
    if pvalues.max() > 0.05:
        features_obj = np.delete(features_obj, pvalues.argmax(),1)
    else:
        
        break
    
    


