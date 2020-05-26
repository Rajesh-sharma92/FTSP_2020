# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\student_scores.csv') 

dataset.isnull().any(axis=0)

# To seggrating the features & lables from dataset.
features = dataset.iloc[:,:-1].values

labels = dataset.iloc[:,1].values

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

df.head()
---------------
   Actual  Predicated
0      20   15.964757
1      69   74.613283
2      17   11.988585
3      85   77.595411
4      60   55.726469





