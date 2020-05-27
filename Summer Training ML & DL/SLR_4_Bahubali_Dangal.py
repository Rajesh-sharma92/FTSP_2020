# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Bahubali2_vs_Dangal.csv') 

dataset.head()
------------------
   Days  Bahubali_2_Collections_Per_day  Dangal_collections_Per_day
0     1                           41.00                       29.78
1     2                           40.50                       34.82
2     3                           46.50                       42.35
3     4                           40.25                       25.48
4     5                           30.00                       23.07


dataset.isnull().any(axis=0)
----------------
Days                              False
Bahubali_2_Collections_Per_day    False
Dangal_collections_Per_day        False
dtype: bool


features = dataset.iloc[:,[0]].values

labels = dataset.iloc[:,[1,2]].values


from sklearn.linear_model import LinearRegression

# Now to create the Object of the LinearReggression
regressor = LinearRegression()

# Now we train the Model to make it easier.
regressor.fit(features,labels)


# We can also predict by using Predict() function also.

print(regressor.coef_*10 + regressor.intercept_) 
#  [[17.41666667  4.90944444]
#  [31.76666667 19.25944444]]


print(regressor.predict([[10]]))
# [[17.41666667 19.25944444]]


print(regressor.predict([[15]]))
-------------------
# [[ 2.25       11.26777778]]


print(regressor.predict([[20]]))
-------------------
# [[-12.91666667   3.27611111]]


----------------------------------------------------------------------------------------------

features = dataset.iloc[:,0:1].values

labels = dataset.iloc[:,[1,2]].values

from sklearn.model_selection import train_test_split

features_train , features_test , labels_train , labels_test =\
train_test_split(features,labels,test_size=0.2,random_state=41)

# Now we apply the Linear Regression.
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)







