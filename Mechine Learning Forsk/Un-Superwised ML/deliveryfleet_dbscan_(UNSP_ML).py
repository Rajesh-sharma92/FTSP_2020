"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) 
and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

Perform K-means clustering to distinguish urban drivers and rural drivers.
Perform K-means clustering again to further distinguish speeding drivers 
from those who follow speed limits, in addition to the rural vs. urban division.
Label accordingly for the 4 groups.

"""
# using db scan

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data=pd.read_csv('E:\ML Code Challenges\ML CSV Files\deliveryfleet.csv')

data.isnull().any(axis=0)

data.info()

features=data.iloc[:,[1,2]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

stscaler = StandardScaler().fit(data)

data = stscaler.transform(data)
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.3, min_samples=10).fit(data)
labels = db.labels_ 


plt.scatter(features[labels== 0,0], features[labels == 0,1],c='red', marker='+' )
plt.scatter(features[labels == 1,0], features[labels == 1,1],c='green', marker='o' )
plt.scatter(features[labels == 2,0], features[labels == 2,1],c='blue', marker='s' )
plt.scatter(features[labels == -1,0],features[labels == -1,1],c='yellow', marker='*' )

