# KMeans Algorithm Clustring Unsuperivised Machine Learnning :- 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv(r'E:\ML Code Challenges\ML CSV Files\xclara.csv')

print(dataset.shape) # (3000, 2)

dataset.head()
---------------------
          V1         V2
0   2.072345  -3.241693
1  17.936710  15.784810
2   1.083576   7.319176
3  11.120670  14.406780
4  23.711550   2.557729

features = dataset.iloc[: , [0,1]].values

dataset.isnull().any(axis=0) # No Missing values as well

# There is No Categorial data.
# There is No Missing data.
# There is No need to perform the feature scaling as well coz data is in correct form.

# Now we will scatter all these data points as well
plt.scatter(features[:,0] , features[:,1] , color='Blue')
plt.show()

# fitting KMeans to Dataset by 3 clusters.
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3 , init='k-means++',random_state=0)

pred_cluster = kmeans.fit_predict(features)

print(pred_cluster) # [2 2 2 ... 0 0 0] # It is belongs to all 3 cluster Nos. like 0,1,2.

# Visualizing the Clusters Nos.
features[pred_cluster == 0]
print(len(features[pred_cluster == 0])) # 952

features[pred_cluster == 0 ,0]

len(features[pred_cluster == 0,0]) # 952

len(features[pred_cluster == 1]) # 1149

plt.scatter(features[pred_cluster == 0,0] , features[pred_cluster == 0,1] , c='Blue' , label = 'Cluster1')
plt.scatter(features[pred_cluster == 1,0] , features[pred_cluster == 1,1], c='Red' , label = 'Cluster2')
plt.scatter(features[pred_cluster == 2,0] , features[pred_cluster == 2,1], c='Green' , label = 'Cluster3')
plt.legend()

''' Centroid of the Clusters 
# Centroid : Center of Mass.

Centroid of X =         Sum of X Coordinates
                     -------------------------
                        Total No. of Values
                   
                   
Centroid of Y =        Sum of Y Coordinates
                    -------------------------
                       Total No. of Values
                       
'''

print(kmeans.cluster_centers_)    # There are 2 Clusters.
***********************
[[ 69.92418447 -10.11964119]
 [ 40.68362784  59.71589274]
 [  9.4780459   10.686052  ]]

print(kmeans.cluster_centers_[:,0]) # x [69.92418447 40.68362784  9.4780459 ]

print(kmeans.cluster_centers_[:,1]) # y [-10.11964119  59.71589274  10.686052  ]

plt.scatter(features[pred_cluster == 0,0] , features[pred_cluster == 0,1] , c='Blue' , label = 'Cluster1')
plt.scatter(features[pred_cluster == 1,0] , features[pred_cluster == 1,1], c='Red' , label = 'Cluster2')
plt.scatter(features[pred_cluster == 2,0] , features[pred_cluster == 2,1], c='Green' , label = 'Cluster3')
plt.scatter(kmeans.cluster_centers_[:,0] , kmeans.cluster_centers_[:,1], c='Yellow' , label = 'Centroid')
plt.legend()                   
                       
plt.title('Clusters of DataPoints')                      
plt.xlabel('X Coordinates')
plt.ylabel('Y Coordinates')
plt.show()


''' WCSS :- With in Cluster Sum of Square. '''


# Now we will see that how we can calculate the No. of Culsters.
wcss = [] # Empty List

for i in range(1,11):
    kmeans = KMeans(n_clusters=i , init='k-means++',random_state=0)
    kmeans.fit(features)
    
    wcss.append(kmeans.inertia_)
    
# Now plot it.
plt.plot(range(1,11),wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


    


