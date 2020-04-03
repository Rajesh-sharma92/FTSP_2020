# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:58:49 2020

@author: Rajesh

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

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'E:\ML Code Challenges\ML CSV Files\tshirts.csv')
dataset.head()

# There is no Categorial data
pd.set_option('display.max_columns' , None)
dataset.sample(10)

# There is no Missing data
dataset.isnull().any(axis=0) 
# There is no different scale data

features = dataset.iloc[:,[1,2]].values

#Scatter all these data points on the matplotlib
# It seems as a human that it will have 3 clusters or groups
plt.scatter(features[:,0] , features[:,1])
plt.show()

# Fitting K-Means to the dataset using 3 clusters
from sklearn.cluster import KMeans
# Since we have seen the visual, we have told the algo to make 1 cluster
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)

pred_cluster = kmeans.fit_predict(features) # We have only passed features 

print(pred_cluster) # Its the cluster id with 0 1 and 2 

# How to find which points from features falls with cluster id 0
print(features)
print(pred_cluster)
print(pred_cluster == 0  )
# will gives a True False Array, we will use boolean indexing concept
print(features[pred_cluster == 0])
print(len(features[pred_cluster == 0])) # 48


# How to find which points from features falls with cluster id 1
print(features)
print(pred_cluster == 1  )
# will gives a True False Array, we will use boolean indexing concept
print(features[pred_cluster == 1])
print(len(features[pred_cluster == 1])) # 37

print(features[pred_cluster == 0, 0])  # 0 is for V1

# Will print V2
print(features[pred_cluster == 0, 1])  # 1 is for V2


# Visualising the clusters
# plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')

# Centroid of the clusters 
"""
Explain the concept of Center of Mass = Centroid 

                     Sum of x coordinates 
x of centroid   =   -----------------------
                    Total number of values 
                    

                     Sum of y coordinates 
y of centroid   =   -----------------------
                    Total number of values                     

"""
print(kmeans.cluster_centers_)  # There are three points for 3 centroid

print(kmeans.cluster_centers_[:, 0]) # x 
print(kmeans.cluster_centers_[:, 1]) # y 

# Central Location of the Cluster == Centroid
# Centroid = Avg of x coordinate and Avg of y coordinate for lets assume Cluster 1
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')



plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()



# Using the elbow method to find the optimal number of clusters
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'E:\ML Code Challenges\ML CSV Files\tshirts.csv')

features = dataset.iloc[:, [1, 2]].values
   

from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)  # we have not used the fit_predict
    #print("Cluster " + str(i) +  "  =  " + str(kmeans.inertia_))
    wcss.append(kmeans.inertia_)     # ( calculates wcss for a cluster )
    
print(wcss)

# Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


# Silhouette Score calculation to find optimal number of clusters 

from sklearn.metrics import silhouette_score

for n_clusters in range(2, 11):
    clusterer = KMeans (n_clusters=n_clusters)
    preds = clusterer.fit_predict(features)
    centers = clusterer.cluster_centers_

    score = silhouette_score (features, preds, metric='euclidean')
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", score)

# For n_clusters = 2 The average silhouette_score is : 0.5839500654008686

