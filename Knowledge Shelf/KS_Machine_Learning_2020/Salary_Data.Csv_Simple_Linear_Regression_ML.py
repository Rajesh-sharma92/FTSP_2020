# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:12:19 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\Salary_Data.csv')
dataset.head()
******************
 YearsExperience   Salary
0              1.1  39343.0
1              1.3  46205.0
2              1.5  37731.0
3              2.0  43525.0
4              2.2  39891.0

features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
************
     Actual     Predicated
0   37731.0   41056.257055
1  122391.0  123597.709384
2   57081.0   65443.504334
3   63218.0   63567.562235
4  116969.0  116093.940990
5  109431.0  108590.172597
6  112635.0  117031.912039
7   55794.0   64505.533285

NOTE :- If there the experience is 12 / 15 yrs then what will be the predicated salaries.

x = [12]
x = np.array(x)
x = x.reshape(-1,1)
a = regressor.predict(x)
a[0] # 139543.21722008943

x = [15]
x = np.array(x)
x = x.reshape(-1,1)
a = regressor.predict(x)
a[0] # 167682.34869592747

# We will plot the graph of these values.
# This is for the Training dataset.

plt.scatter(features_train,labels_train,color='blue')
#plt.plot(features_test,regg.predict(features_test),color='orange')
plt.plot(features_train,regressor.predict(features_train),color='orange')
plt.xlabel('No. of Experience')
plt.ylabel('Salaries Details')
plt.title('Experience & Salaries Graph for Training Dataset')
# plt.savefig('')
plt.show()

# This is for the Test dataset.
plt.scatter(features_test,labels_test,color='blue')
#plt.plot(features_test,regg.predict(features_test),color='orange')
plt.plot(features_test,regressor.predict(features_test),color='orange')
plt.xlabel('No. of Experience')
plt.ylabel('Salaries Details')
plt.title('Experience & Salaries Graph for Testing Dataset')
# plt.savefig('')
plt.show()


"""
Equation Results Verification :- 
-----------------------------
"""
We know that we have the straight Line Equation.
y = mx+c

where y is the labels / Predication values / Depandent variable.

x = features / Input variables / Indepandent variable.

m = slope (y2-y1/x2-x1) and mx means x is the co-efficent.

c = Intercept.

# Now here we will be calculating some the salaries values for new employees.

CASE - 1 :- 
------------ 
y = mx+c

print(regressor.coef_) # 9379.71049195

print(regressor.intercept_) # 26986.691316737248

y = (9379.71049195 * 1.5 + 26986.691316737248)
print(y) # 41056.257054662245

y = (9379.71049195 * 10.5 + 26986.691316737248)
print(y) # 125473.65148221224

 












