# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Social_Network_Ads.csv') 

dataset.head()
----------------
   Age  EstimatedSalary  Purchased
0   19            19000          0
1   35            20000          0
2   26            43000          0
3   27            57000          0
4   19            76000          0


dataset.isnull().any(axis=0) # There is Nan Values into Dataset.

# To seggrating the features & lables from dataset.
features = dataset.iloc[:,0:2].values

labels = dataset.iloc[:,2].values

from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test =\
train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()

classifier.fit(features_train,labels_train)

labels_pred = classifier.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})

df.head()
---------------
   Actual  Predicated
0       1           1
1       1           1
2       1           0
3       1           1
4       0           0

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test,labels_pred)
print(cm)
------------
[[65  3]
 [ 8 24]]

print((65+24)/(65+3+8+24)) # 0.89

print(classifier.score(features_train,labels_train)) # 0.8233

print(classifier.score(features_test,labels_test)) # 0.89

# We can check the Accuracy Score as well.
from sklearn.metrics import accuracy_score

Acc_score = accuracy_score(labels_test,labels_pred)
print('Accuracy Score :', Acc_score) # Accuracy Score : 0.89


Precision Score =         TP
                     ----------------
                         TP + FP

from sklearn.metrics import precision_score

print(precision_score(labels_test,labels_pred,pos_label=0)) # 0.8904
print(precision_score(labels_test,labels_pred,pos_label=1)) # 0.888


# To define Recall score / Sensitivity.
Recall =        TP
           -------------- 
               TP + FN
               
from sklearn.metrics import recall_score 

print(recall_score(labels_test,labels_pred,pos_label=0)) # 0.95
print(recall_score(labels_test,labels_pred,pos_label=1)) # 0.75

# To calculating the f1 score.
from sklearn.metrics import f1_score

print(f1_score(labels_test,labels_pred,pos_label=0)) # 0.92
print(f1_score(labels_test,labels_pred,pos_label=1)) # 0.81



# If we want at a time all these above functions then we can go for Classification Report.
from sklearn.metrics import classification_report

print(classification_report(labels_test,labels_pred))             
------------------------------------
             precision    recall  f1-score   support

           0       0.89      0.96      0.92        68
           1       0.89      0.75      0.81        32

    accuracy                           0.89       100
   macro avg       0.89      0.85      0.87       100
weighted avg       0.89      0.89      0.89       100

print(classification_report(labels_test,labels_pred,target_names=['Yes','No']))             
-------------------------------
             precision    recall  f1-score   support

         Yes       0.89      0.96      0.92        68
          No       0.89      0.75      0.81        32

    accuracy                           0.89       100
   macro avg       0.89      0.85      0.87       100
weighted avg       0.89      0.89      0.89       100

-------------------------------------------------------------------------------------------------
''' By Using the Simple Linear Regression '''

# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Social_Network_Ads.csv') 

dataset.head()
----------------
   Age  EstimatedSalary  Purchased
0   19            19000          0
1   35            20000          0
2   26            43000          0
3   27            57000          0
4   19            76000          0


dataset.isnull().any(axis=0) # There is Nan Values into Dataset.

# To seggrating the features & lables from dataset.
features = dataset.iloc[:,0:2].values

labels = dataset.iloc[:,2].values

from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test =\
train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)


# Now we apply the Linear Regression.
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)

df.head()

print(type(labels_pred)) # <class 'numpy.ndarray'>

print(regressor.score(features_train,labels_train)) # 0.43

print(regressor.score(features_test,labels_test)) # 0.54

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test,labels_pred)
print(cm) # Here we can not able to find out the how many people have clicked or not.







