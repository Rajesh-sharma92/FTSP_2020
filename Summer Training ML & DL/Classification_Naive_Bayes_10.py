# It is the classification Problem.
"""
Naive Bayes flavour ( variants )
    1. Gaussian     ( for continuous data like numerical )
    2. Bernolli     ( for discrete values like 0 or 1 )
    3. Multinomial  ( for text data like NLP )
"""
     
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv(r'E:\ML Code Challenges\ML CSV Files\training_titanic.csv')

print(dataset.shape) # (891, 12)

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

# Convert categorical variable to numeric ( Label Encoding )
# Label Encoding using numpy

dataset['sex_cleaned'] = np.where(dataset['Sex']=='male',0,1)

dataset.shape # (891, 13)

dataset['Embarked_cleaned'] = np.where(dataset['Embarked']=='S',0,
       np.where(dataset['Embarked']=='C',1,
                np.where(dataset['Embarked']=='Q',2,3)
                )
       )
       
# S == 0  C == 1  Q == 2  any other == 3
print(dataset.shape) # (891, 14)

# Cleaning dataset of NaN
# This will delete the data which has categorical data and missing rows.
dataset = dataset[["Survived",
                  "Pclass",
                  "sex_cleaned",
                  "Age",
                  "SibSp",
                      "Parch",
                      "Fare",
                      "Embarked_cleaned"]].dropna(axis = 0 , how = 'any') # # any and all reference to the columns
       

dataset.shape # (714, 8)

# Split dataset in training and test datasets
from sklearn.model_selection import train_test_split

# We have not seperated the feature and label, we have given the whole data
# thats why we only have features test and train 
# we have taken care where we are training the model in fit method
features_train,features_test = train_test_split(dataset,test_size=0.5,random_state=0)
#  we are passing full data as features and no labels are passed

gnb = GaussianNB()

used_features  = ["Pclass",
                  "sex_cleaned",
                  "Age",
                  "SibSp",
                      "Parch",
                      "Fare",
                      "Embarked_cleaned"]

                        # "Survived" cloumn is used for labeling.
                        
gnb.fit(features_train[used_features].values, # features are passed 
        features_train['Survived'].values # labels is passed
        )

labels_pred = gnb.predict(features_test[used_features])                        
                        
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_gnb = confusion_matrix(features_test["Survived"], labels_pred)
print(cm_gnb)
*******************
[[174  37]
 [ 47  99]]

print((174+99)/(174+37+47+99)) # 0.76

--------------------------------------------------------------------------------------------------
# Multinimial Algorithm.

mnb = MultinomialNB()

used_features =[

    "Pclass",
    "sex_cleaned",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked_cleaned"
   
]

# Train classifier
mnb.fit(
    features_train[used_features].values,
    features_train["Survived"].values
)
labels_pred = mnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_mnb = confusion_matrix(features_test["Survived"], labels_pred)
print(cm_mnb)
******************
[[170  41]
 [ 77  69]]

print((170+69)/(170+41+77+69)) # 0.66

-------------------------------------------------------------------------------------------------
# Barnoli Algorithm.

bnb = BernoulliNB()
used_features =[

    "Pclass",
    "sex_cleaned",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked_cleaned"
   
]

# Train classifier
bnb.fit(
    features_train[used_features].values,
    features_train["Survived"]
)
labels_pred = bnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_bnb = confusion_matrix(features_test["Survived"], labels_pred)
print(cm_bnb)
***********************
[[163  48]
 [ 42 104]]

print((163+104)/(163+48+42+104)) # 0.74








