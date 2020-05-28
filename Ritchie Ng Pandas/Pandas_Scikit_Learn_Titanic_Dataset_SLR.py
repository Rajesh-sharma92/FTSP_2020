# Pandas and Scikit-Learn
# Using pandas with scikit-learn effecticent.

import pandas as pd

url = 'http://bit.ly/kaggletrain'

dataset = pd.read_csv(url)

dataset.head()
--------------------
  PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

dataset.isnull().any(axis=0) # There are so Nan Values available.

features_cols = ['Pclass' , 'Parch']

features = dataset.loc[: , features_cols].values

labels = dataset.loc[: , ['Survived']].values

from sklearn.model_selection import train_test_split

features_train , features_test , labels_train , labels_test =\
train_test_split(features,labels,test_size=0.2,random_state=41)


from sklearn.linear_model import LogisticRegression

regressor = LogisticRegression()

regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

regressor.predict([[3,0]])

regressor.predict([[3,1]])

regressor.predict([[3,3]]) 


df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)






