# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\student_scores.csv') 

# To get first 5 records from DS
dataset.head()
-------------------
   Hours  Scores
0    2.5      21
1    5.1      47
2    3.2      27
3    8.5      75
4    3.5      30

# Explore the Dataset
dataset.shape # (25, 2)

dataset.ndim  # 2

dataset.size # 50 

dataset.columns # Index(['Hours', 'Scores'], dtype='object')

dataset.values # To get the values into ndarray.

dataset.dtypes
------------------
Hours     float64
Scores      int64
dtype: object

dataset.describe()
------------------------
           Hours     Scores
count  25.000000  25.000000
mean    5.012000  51.480000
std     2.525094  25.286887
min     1.100000  17.000000
25%     2.700000  30.000000
50%     4.800000  47.000000
75%     7.400000  75.000000
max     9.200000  95.000000


# Check if any NaN values into Dataset.
dataset.isnull().any(axis=0)
---------------
Hours     False
Scores    False
dtype: bool

# To seggrating the features & lables from dataset.
features = dataset.iloc[:,:-1].values

labels = dataset.iloc[:,1].values

''' Now we will use the LinearReggression Algorithm to train the Model '''

from sklearn.linear_model import LinearRegression

# Now to create the Object of the LinearReggression
regressor = LinearRegression()

# Now we train the Model to make it easier.
regressor.fit(features,labels)

print(regressor.intercept_) # 2.483673405373196 # c

print(regressor.coef_) # [9.77580339] # m

# We know that , y = mx + c

print(regressor.coef_*10 + regressor.intercept_) # [100.24170731]

# We can also predict by using Predict() function also.

x = 20
print(type(x)) # int type.
x = [20]
x = np.array(x)
print(x.ndim) # 1
x = x.reshape(1,1)
print(x.ndim) # 2
print(regressor.predict(x))  # [100.24170731]


# print(regressor.predict([[20]])) # [197.24170731]

plt.scatter(features,labels,color='Green')
plt.plot(features,regressor.predict(features), color = 'Red')
plt.title('Study Hours and Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score: Marks')
# plt.savefig('E:\Mechine Learning Forsk\Marks_Scores1.jpg')
plt.show()





