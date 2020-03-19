# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:33:35 2020

@author: Rajesh
"""
# Focus is on Supervised Machine Learning
# But on Classification and not Regression
# We need to predict a category and not a value in classification 
# Logistic Regression 
# K Nearest Neighbour  kNN

# Importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# How many hours the student studied
HOURS = [0.50,0.75,1.00,1.25,1.50,1.75,2.00,2.25,2.50,2.75,3.00,3.25,3.50,3.75,4.00,4.25,4.50,4.75,5.00,5.50]
print(len(HOURS))

# Whether he passed or failed ?
PASS = [0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1]
print(len(PASS))

# Try to understand the plot
# If the student is studying less, then he is FAILED and is on lower line
# If the student is studying more, then he is PASSED and he is on upper line
plt.scatter(HOURS, PASS)


# Can we apply Linear Regression to such problem
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  

# Converted the data into NDArray
regressor.fit(np.array(HOURS).reshape(-1,1), np.array(PASS).reshape(-1,1)) 

#Visualize the best fit line
import matplotlib.pyplot as plt

# Visualising the  results
plt.scatter(HOURS, PASS, color = 'red')
plt.plot(HOURS, regressor.predict(np.array(HOURS).reshape(-1,1)), color = 'blue')
plt.title('Study Hours and Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score: Marks')
plt.show()

"""
LR will predict us continuous values, so it would not be only 0 and 1
but also the fractional values between 0 and 1
It seems now that our problem cannot be solved throught LR
So we require such a algorithm which will predict only 0 or 1 
and not the values between them or continuous values

For solving such a problem we will not use the LR algorithm 
but use Logistic Regression Algorithm

Linear Regression range would be less than 0 and more then 1 also
But in Logistic Regression it will only be either 0 or 1
"""


# Show image linear_vs_logistic_regression.jpg

"""
If we taper the upper and lower end such that they do not go beyond zero
in the lower range and they do not go beyond 1 in the upper range

What will happen for those points on x which maps to .2 on y  and similar case for .8 ?


This function shows the probability ( Hone yaa na hone ke )
IF probability is .5 and less then it makes in 0
If the probability is more then .5 then it makes it 1

So logistic Regression gives us Probablity and if the probability is .5 and less 
then it gives us 0 and if the probability is more then .5, it gives us 1

This function which is shown is a famous funciton and is known as Sigmoid Function 
So our mapping function is not a Straight line but a sigmoid function.

So the basic algorithm for Classification is the Logistic Regression
Generally the problems around our life are classification problem
India Jetegi and nahi ?
Hoga yaa nahi ?
Placement Hoga ya Nahi ?
Movie Hit hogi ya Nahi ?
Customer chod ke jayega ya Nahi ?


80% problems in the Industry are classification problems

"""


# Now try to solve a problem

# Dataset from UCI Repository 
# https://archive.ics.uci.edu/ml/index.php
# Or Kaggle.com
# https://www.hackerrank.com/ 
# https://www.hackerearth.com/
# TCS Hiring Through CodeVita
# More Package through Digital Hiring Platfrom
# 


# Open the Heart_Disease.csv from UCI Repository 
# We are predicting his hearth Disease with 1 or 0 as the Class in last column
# There are v1 to v9 total 9 features 
# ML Algo works on the column data and it does not known what that means
# 


import sklearn as sk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
We will look at data regarding coronary heart disease (CHD) in South Africa. 
The goal is to use different variables such as tobacco usage, family history, 
ldl cholesterol levels, alcohol usage, obesity and more.
"""


heart = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Heart_Disease.csv', sep=',',header=0)  


# There is no Categorical Data
heart.head()
heart.sample(5)


# There is no Missing Data
# Check Column wise is any data is missing or NaN
heart.isnull().any(axis=0)

# Lets seperate the features and labels from the data 
features = heart.iloc[:,:9].values
print(features)

labels = heart.iloc[:,[9]].values 
print(labels)


"""
# Show the features data in the Variable Explorer
# Pre processing last activity is Feature scaling
# Our algo works on magnitude and not on unit
# Column which is in high range ( that means magnitude is HIGH)
# That column in more IMPORTANT
# We do not want that , all column should be treated EQUALLY
# We need to transform the data into another format
# Lot of variation in the columns data 
# This process in known as Feature Scaling

Two different teachers of your teaching different subject 
They take a suprise test of their subjects 
One for 100 marks and others on 10 marks scale
They now need to show a combined result
We need to convert the 100 scale to 10 or vice versa

There are two ways in ML to do feature scaling
1. Min Max Scaling
2. Standard Scaling


Standard Scaling
We find the mean of the column (mean)
We find the standard deviation of the column (std)

We then calculate the each values in the column using the below formula and replace it
(x - mean ) / std

All values becomes normally distributed 
We know that Normally distributed has a Bell Curve 
mean becomes 0 and standard deviation becomes 1
Some values becomes positive and some negative

We then apply on each columns
Values coming from Dummy variables also needs to be featured scaled



Min Max Scaling
( x - min) / ( max - min )
All the values will come between 0 and 1


For Machine Learning we use Standard Scaling
For Deep Learning we use Min Max Scaling

Inverse Transform can be used to again bring back the data after scaling

"""

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)



# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)

# He has already calculated the mean and sd, so we only need to transform
features_test = sc.transform(features_test)



# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)


# There are two menthods
# 


#Calculate Class Probabilities
# Open in variable explorer and show ( FAIL and PASS probability)
# There are two probabilities since we have 2 class
probability = classifier.predict_proba(features_test)
print(probability)


# Predicting the class labels ( 0 or 1 )
labels_pred = classifier.predict(features_test)

# Comparing the predicted and actual values
my_frame= pd.DataFrame(labels_pred, labels_test)
print(my_frame)



# Now we can draw 4 combination 
# I predicted 1 , Acutal was also 1  ( RIGHT PREDICTION ) True positives (TP)
# I predicted 2,  Actual was also 2  ( RIGHT PREDICTION ) True negatives (TN)

# I predicted 1 , Acutal was also 2  ( WRONG PREDICTION ) False positives (FP)
# I predicted 2,  Actual was also 1  ( WRONG PREDICTION ) False negatives (FN)

# We represent this type of information in form of Matrix


# Making the Confusion Matrix or Error Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

"""
   1   2   ( predicted)
1 [68  9]
2 [19 20]

68 + 20  ( RIGHT PREDICTION )
19 + 9   ( WRONG PREDICTION )

"""

# Model Score = 75.86 times out of 100 model prediction was RIGHT
print( (68.0 + 20.0) / 116.0) # 0.7586206896551724



"""
Steps in Data Preprocessing

Step 1 : Import the libraries
Step 2 : Import the data-set
Step 3 : Check out the missing values - imputation using sklearn, pandas
Step 4 : Label encoding - categorical data using LabelEncoder, cat.code (category)
Step 5 : order issue - onehotencoding (dummy encoding) - OneHotEncoder, get_dummies
Step 6 : Splitting the data-set into Training and Test Set
Step 7 : Feature Scaling

80% of time is consumed in pre processing 
weka is a tool of drag and drop for ML projects

----------------------------------------------------------------------------------------------




















