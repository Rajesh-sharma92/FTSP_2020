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
-----------
 Actual  Predicated
0      20   15.964757
1      69   74.613283
2      17   11.988585
3      85   77.595411
4      60   55.726469

df.head()

''' Now we will be calculating Performance Measurement '''
# Evaluate the Algorithms.

from sklearn import metrics

print('Means Absolute Error(MAE) :', metrics.mean_absolute_error(labels_test , labels_pred))
# Means Absolute Error(MAE) : 5.267612082160115

print('Mean Squared Error(MSE) :', metrics.mean_squared_error(labels_test , labels_pred))
# Mean Squared Error(MSE) : 29.199482214072795

print('Root Mean Squared Error(RMSE) :', np.sqrt(metrics.mean_squared_error(labels_test , labels_pred)))
# Root Mean Squared Error(RMSE) : 5.403654523937739

print(np.mean(dataset.values[:,1])) # 51.48  # 10% of 51.48 = 5.15

dataset['Scores'].mean() # 51.48

# RMSE < np.mean(labels)*10%

# NOTE :- If the above condition satisfy then  our Model is correct & prediction also fine.

print('R Squared Error(R2 Score):', metrics.r2_score(labels_test , labels_pred))
# R Squared Error(R2 Score): 0.9602706511727539

# NOTE :- Max R2 score is the 1. 
# In our case we have got 0.96 and it is almost nearest to 1 only.
# It is very good model & best model which R2 score is almost nearest by 1.


''' To get the Model Accuracy ''' 

print(regressor.score(features_test , labels_test)) # 0.96027

print(regressor.score(features_train , labels_train)) # 0.94946

# Underfitting :- training score is poor & test score is also poor.

# Overfitting :- training score is Good & test score is poor.

# NOTE :- Neither our model should not be the Underfitting nor Overfitting as well.

# To fix such issues we have to follow some points like below listed.

# In the case of Underfitting we can do one thing that Increase the Training data and then 
# Obvisouly the Test score will be more the ealier.


# In the case of Overfitting there we have some other technique to get the better test score.
# We need to apply the Regularazation to avoid Overfitting issue at data.

1) L1 (Lasso)
2) L2 (Ridge)
3) Elastic Net (L1+l2)





