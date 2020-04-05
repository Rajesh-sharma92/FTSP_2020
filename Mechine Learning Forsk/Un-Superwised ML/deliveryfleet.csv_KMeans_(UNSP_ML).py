# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:38:33 2020

@author: Rajesh
"""
"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) 
and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

1) Perform K-means clustering to distinguish urban drivers and rural drivers.

2) Perform K-means clustering again to further distinguish speeding drivers 
from those who follow speed limits, in addition to the rural vs. urban division.
Label accordingly for the 4 groups.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\deliveryfleet.csv')
dataset.head()

dataset['Distance_Feature'].mean() # 76.04152250000006

dataset['Speeding_Feature'].mean() # 10.721

features = dataset.iloc[:, [1,2]].values

# There is no Categorial data.
pd.set_option('display.max_columns' , None)
dataset.sample(10)

# NOTE :- If there is No Categorial dat then No need to perform any kind of operations like
# Label encoding and OneHot encoding.

# There is no Missing data .
dataset.isnull().any(axis=0) # We don't have any missing values into dataset.

# Scatter all these data points on the matplotlib
# It seems as a human that it will have 3 clusters or groups

plt.scatter(features[:,0] , features[:,1])
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2 , init = 'k-means++' , random_state = 0)

pred_cluster = kmeans.fit_predict(features)
print(pred_cluster) # Its the cluster id with 0 & 1.
# [0 0 0 ... 1 1 1]

# How to find which points from features falls with cluster id 0
print(features)
print(pred_cluster)
print(pred_cluster == 0  )
# will gives a True False Array, we will use boolean indexing concept
print(features[pred_cluster == 0])
print(len(features[pred_cluster == 0])) # 3200


# How to find which points from features falls with cluster id 1
print(features)
print(pred_cluster == 1  )
# will gives a True False Array, we will use boolean indexing concept
print(features[pred_cluster == 1])
print(len(features[pred_cluster == 1])) # 800

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
print(kmeans.cluster_centers_)  # There are three points for 2 centroid

print(kmeans.cluster_centers_[:, 0]) # x 
print(kmeans.cluster_centers_[:, 1]) # y 

# Central Location of the Cluster == Centroid
# Centroid = Avg of x coordinate and Avg of y coordinate for lets assume Cluster 1
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Urban')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')

plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
# plt.savefig('E:\Mechine Learning Forsk\Un-Superwised ML\Deliveryfleet_Centroid')
plt.show()


# Using the elbow method to find the optimal number of clusters.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'E:\ML Code Challenges\ML CSV Files\Deliveryfleet.csv')

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

-------------------------------------------------------------------------------------------
"""
2) Perform K-means clustering again to further distinguish speeding drivers 
from those who follow speed limits, in addition to the rural vs. urban division.
Label accordingly for the 4 groups.
"""
 

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)

features = dataset.iloc[:, [1,2]].values

pred_cluster = kmeans.fit_predict(features) 

print(pred_cluster) # Its the cluster id with 0,1,2,3 

print(features[pred_cluster == 0])

print(features[pred_cluster == 1])

print(features[pred_cluster == 2])

print(features[pred_cluster == 3])


# Visualising the clusters
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Follow speed in Rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Not follow speed in Urban')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Follow speed in Urban')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'olive', label = 'Not follow speed in Rural')


print(kmeans.cluster_centers_)  # There are two points for 2 centroid   Rural follow speed

print(kmeans.cluster_centers_[:, 0]) 
print(kmeans.cluster_centers_[:, 1])
# Central Location of the Cluster == Centroid

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')


plt.title('Clusters of datapoints')
plt.xlabel('Distance')
plt.ylabel('Speed')
plt.legend()
plt.show()











