# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Salary_Classification.csv') 

dataset.head()
--------------------
    Department  WorkedHours  Certification  YearsExperience  Salary
0  Development         2300              0              1.1   39343
1      Testing         2100              1              1.3   46205
2  Development         2104              2              1.5   37731
3           UX         1200              1              2.0   43525
4      Testing         1254              2              2.2   39891


dataset.isnull().any(axis=0) # There is No Nan Values into Dataset.

# To seggrating the features & lables from dataset.

features = dataset.iloc[:,:-1].values

labels = dataset.iloc[:,-1].values

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ColumnTransformer = ColumnTransformer([('encoder',OneHotEncoder(),[0])], remainder = 'passthrough')

features = np.array(ColumnTransformer.fit_transform(features) , dtype = np.float32)

# Avoiding the Dummy Variable Trap.
# Dropping first column.
features = features[: , 1:]

from sklearn.model_selection import train_test_split

features_train , features_test , labels_train , labels_test =\
train_test_split(features,labels,test_size=0.2,random_state=41)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(features_train,labels_train)

# Now we will be predicating the Test set data.
labels_pred = regressor.predict(features_test)

# To get the Predictions into Dataframe.
df = pd.DataFrame({'Actual':labels_test , 'Predicatd':labels_pred})
print(df)
--------------
   Actual      Predicatd
0   55794   62876.070312
1  121872  126866.460938
2   63218   58750.777344
3   91738   86498.460938
4  116969  111905.414062
5   56642   52411.207031

# Now we will be doing the Predictions for new Values.
x = ['Development',1150,3,4]

print(type(x)) # <class 'list'>

x = np.array(x)

print(type(x)) # <class 'numpy.ndarray'>

print(x.shape) # (4,)

x = x.reshape(1,4) # x.reshape(1,-1)

print(x.shape) # (1, 4)

x = np.array(ColumnTransformer.transform(x) , dtype = np.float32)

x = x[: , 1:]

regressor.predict(x) # [61993.06]

------------------------------------------------------------------------------------------

# Now we will be doing the Predictions for new Values.
x = ['Testing',1000,2,2]

print(type(x)) # <class 'list'>

x = np.array(x)

print(type(x)) # <class 'numpy.ndarray'>

print(x.shape) # (4,)

x = x.reshape(1,4) # x.reshape(1,-1)

print(x.shape) # (1, 4)

x = np.array(ColumnTransformer.transform(x) , dtype = np.float32)

x = x[: , 1:]

regressor.predict(x) # [39282.37]

--------------------------------------------------------------------------------------------

# Now we will be doing the Predictions for new Values.
x = ['UX',1200,3,8]

print(type(x)) # <class 'list'>

x = np.array(x)

print(type(x)) # <class 'numpy.ndarray'>

print(x.shape) # (4,)

x = x.reshape(1,4) # x.reshape(1,-1)

print(x.shape) # (1, 4)

0 , 0 , 1 , 1200 , 3 , 8 

0 , 1 , 1200 , 3 , 8 

x = np.array(ColumnTransformer.transform(x) , dtype = np.float32)

x = x[: , 1:]

regressor.predict(x) # [99553.16]






