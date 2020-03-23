# -*- coding: utf-8 -*-
"""
@author: Rajesh
"""
"""
Code Challenge 

Q1. (Create a program that fulfills the following specification.)
mushrooms.csv
Import mushrooms.csv file
This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one.
Attribute Information:
classes: edible=e, poisonous=p (outcome)
cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s
cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
bruises: bruises=t, no=f
odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s
gill-attachment: attached=a,descending=d,free=f,notched=n
gill-spacing: close=c,crowded=w,distant=d
gill-size: broad=b,narrow=n\
gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,
green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
stalk-shape: enlarging=e,tapering=t
stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?
stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s
stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s
stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y
veil-type: partial=p,universal=u
veil-color: brown=n,orange=o,white=w,yellow=y
ring-number: none=n,one=o,two=t
ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z
spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y
population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y
habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d
Perform Classification on the given dataset to predict if the mushroom is edible or poisonous w.r.t. it’s different attributes.
(you can perform on habitat, population and odor as the predictors)
Check accuracy of the model.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\mushrooms.csv')
print(dataset)

dataset.columns # 23

dataset.dtypes # All are strings types like Object.

dataset.ndim # 2

dataset.isnull().any(axis=0) # False
dataset.isnull().any(axis=0).count() # false = 23 columns


features = dataset.iloc[:,[5,21,22]].values
labels = dataset.iloc[:, [0]].values


# Encoding categorical data
#For label ---> Label encoding
from sklearn.preprocessing import LabelEncoder

# Create objct of LabelENcoder
labelencoder = LabelEncoder()

# Fit and Use the operation Transform
labels[:, 0] = labelencoder.fit_transform(labels[:, 0])   #poisonous = 1, eldible = 0



#For features ----> Label Encoding
for i in range(3):
    features[:, i] = labelencoder.fit_transform(features[:, i])


#onehotEncoding
#For features   -----> onehotEncoding
from sklearn.preprocessing import OneHotEncoder
# Creation of Object




#for ---->  column = 0
onehotencoder = OneHotEncoder(categorical_features = [0])
# Convert to NDArray format
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]




#for ---->  column = 1
onehotencoder = OneHotEncoder(categorical_features = [8])
# Convert to NDArray format
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]





#for ---->  column = 2
onehotencoder = OneHotEncoder(categorical_features = [13])
# Convert to NDArray format
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]





from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)



# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

labels_train = labels_train.astype(float)
# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)


#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)
labels_test = labels_test.astype(float)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

print((1056+965)/2031) # 0.9950


"""
Output:-
[[1056    0]
 [  10  965]]

Accuracy of model = 0.9950763170851797

"""





















