# PCA ( Principal Component Analysis ) # It is used for Dimension Reduction.

# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Wine.csv') 

dataset.head()
********************
   Alcohol  Malic_Acid   Ash  ...  OD280  Proline  Customer_Segment
0    14.23        1.71  2.43  ...   3.92     1065                 1
1    13.20        1.78  2.14  ...   3.40     1050                 1
2    13.16        2.36  2.67  ...   3.17     1185                 1
3    14.37        1.95  2.50  ...   3.45     1480                 1
4    13.24        2.59  2.87  ...   2.93      735                 1

# To seperating the features & labels.
features = dataset.iloc[:,:13].values

labels = dataset.iloc[:,13].values

from sklearn.model_selection import train_test_split

features_train , features_test , labels_train , labels_test =\
train_test_split(features,labels,test_size=0.25,random_state=0)

# Now we do the Feature Scaling here with features_train.
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

print(features_train.shape) # (133, 13)

print(features_test.shape) # (45, 13)

# Now we will be Applying the Dimension Reduction Algorithm on Features dataset.
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)

features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)

print(features_train.shape) # (133, 2)

print(features_test.shape) # (45, 2)

# After dimension Reduction we have just seen that We will be having the Loss 
# & Retaining of the Data.
explained_variance = pca.explained_variance_ratio_

print(explained_variance) # [0.37281068 0.18739996]

# Now we will be applying the Logistic Regression on Retaining Dataset.
# Actually, we have lost 56 % of data due to Dimension Reduction.
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()

classifier.fit(features_train,labels_train)

# Predicting the class labesl like (0 or 1)
labels_pred = classifier.predict(features_test)

# Making Dataframe & doing the Comparison.
df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})

df.head()
-------------
  Actual  Predicated
0       1           1
1       3           3
2       2           2
3       1           1
4       2           2

# Now Check on Confusion Matrix.
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test , labels_pred)

print(cm)
*************
[[16  0  0]
 [ 1 20  0]
 [ 0  0  8]]




