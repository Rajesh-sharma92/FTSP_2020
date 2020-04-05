# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:51:22 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\50_Startups.csv')
dataset.head()
*****************
  R&D Spend  Administration  Marketing Spend       State     Profit
0  165349.20       136897.80        471784.10    New York  192261.83
1  162597.70       151377.59        443898.53  California  191792.06
2  153441.51       101145.55        407934.54     Florida  191050.39
3  144372.41       118671.85        383199.62    New York  182901.99
4  142107.34        91391.77        366168.42     Florida  166187.94

features = dataset.iloc[:,:4].values
labels = dataset.iloc[:,4].values

# Here we can check the categorial columns.
pd.set_option('display.max_columns' , None)
dataset.head(10)
# If we have categorial columns then first we  need to convert into Label encoding then 
# OneHotEncoder system to changes into 0 & 1.

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
features[:,3] = le.fit_transform(features[:,3])
print(features[:,3])

from sklearn.preprocessing import OneHotEncoder
oneHE = OneHotEncoder(categorical_features = [3])
features = oneHE.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[ : , 1:]
# Now our data is ready for Modelling .


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.30,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
************
       Actual     Predicated
0   103282.38  104282.764722
1   144259.40  132536.884992
2   146121.95  133910.850078
3    77798.83   72584.774894
4   191050.39  179920.927619
5   105008.31  114549.310792
6    81229.06   66444.432613
7    97483.56   98404.968401
8   110352.25  114499.828086
9   166187.94  169367.506399
10   96778.92   96522.625400
11   96479.51   88040.671829
12  105733.54  110949.994055
13   96712.80   90419.189785
14  124266.90  128020.462501

# Getting Score for the Multi Linear Reg model
Score = regressor.score(features_train, labels_train) # 0.94726222590345

Score1 = regressor.score(features_test, labels_test) # 0.9818745195074237


"""
If the training score is POOR and test score is POOR then its underfitting
If the training score is GOOD and test score is POOR then its overfitting
"""














