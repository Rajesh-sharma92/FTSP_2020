# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Match_Making.csv') 

dataset.head()
---------------------
  Female_Age  Male_Age  Match
0          24        30      1
1          30        40      1
2          22        49      0
3          43        39      1
4          23        30      1

features = dataset.iloc[:,:-1].values

labels = dataset.iloc[:,-1].values

dataset.isnull().any(axis=0) # There is NaN Values into dataset.

from sklearn.model_selection import train_test_split

features_train , features_test , labels_train , labels_test =\
train_test_split(features,labels,test_size=0.3 ,random_state=41)


# Now we will applying the SVM Algprithm.
from sklearn.svm import SVC
# svm( SVC for classification & SVR for Regression )

classifier = SVC(kernel = 'poly' , random_state = 0)

classifier.fit(features_train , labels_train)

labels_pred = classifier.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})

print(df)


# now we will be making the Confusion Matrix.
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test , labels_pred)

print(cm)
----------------
[[ 31   0]
 [  6 113]]

print((25+69)/(100))  # 0.96


# Now we have done the predictions as per User New Requirements.
x = [22,30]
print(type(x))
x = np.array(x)
x = x.reshape(1,2)
print(classifier.predict(x)) # [1]

x = [24,45]
print(type(x))
x = np.array(x)
x = x.reshape(1,2)
print(classifier.predict(x)) # [0]


x = [24,30]
print(type(x))
x = np.array(x)
x = x.reshape(1,2)
print(classifier.predict(x)) # [1]


x = [21,40]
print(type(x))
x = np.array(x)
x = x.reshape(1,2)
print(classifier.predict(x)) # [0]


x = [10,29]
print(type(x))
x = np.array(x)
x = x.reshape(1,2)
print(classifier.predict(x)) # [0]



x = [50,100]
print(type(x))
x = np.array(x)
x = x.reshape(1,2)
print(classifier.predict(x)) # [0]


x = [90,100]
print(type(x))
x = np.array(x)
x = x.reshape(1,2)
print(classifier.predict(x)) # [1]





