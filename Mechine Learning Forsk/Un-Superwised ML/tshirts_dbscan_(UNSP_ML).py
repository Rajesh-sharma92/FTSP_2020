"""
Q2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height 
and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. 
How would you figure out the actual size of these 3 types of shirt to better 
fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of 
the data as stated above.

by dbscan method
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


data=pd.read_csv(r"E:\ML Code Challenges\ML CSV Files\tshirts.csv")

data.isnull().any(axis=0)

data.info()

features=data.iloc[:,[1,2]].values

plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import DBSCAN

#db = DBSCAN(eps=1, min_samples=5).fit(features[:,-1:-3:-1])
db = DBSCAN(eps=1, min_samples=5).fit(features)
labels = db.labels_ 


plt.scatter(features[labels== 0,0], features[labels == 0,1],c='red', marker='+' )
plt.scatter(features[labels == 1,0], features[labels == 1,1],c='green', marker='o' )
plt.scatter(features[labels == 2,0], features[labels == 2,1],c='blue', marker='s' )
plt.scatter(features[labels == -1,0],features[labels == -1,1],c='yellow', marker='*' )
