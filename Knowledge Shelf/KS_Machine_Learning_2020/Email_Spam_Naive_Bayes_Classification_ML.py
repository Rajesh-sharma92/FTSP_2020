# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:22:48 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\spam.csv')
dataset.head()
*******************
  Category                                            Message
0      ham  Go until jurong point, crazy.. Available only ...
1      ham                      Ok lar... Joking wif u oni...
2     spam  Free entry in 2 a wkly comp to win FA Cup fina...
3      ham  U dun say so early hor... U c already then say...
4      ham  Nah I don't think he goes to usf, he lives aro...

# It shows the all details for the category values.
dataset.groupby('Category').describe()

# How to check the emailis spam or not ?
dataset['spam'] = dataset['Category'].apply(lambda x : 1 if x=='spam' else 0)
dataset.head()


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
train_test_split(dataset.Message,dataset.Category,test_size=0.20,random_state=0)


from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
features_train_count = v.fit_transform(features_train.values)
features_train_count.toarray()[:2]

from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(features_train_count,labels_train)

emails = [
    'Hey mohan, can we get together to watch footbal game tomorrow?',
    'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!'
]
emails_count = v.transform(emails)
mnb.predict(emails_count)

features_test_count = v.transform(features_test)
mnb.score(features_test_count, labels_test) # 0.9865

-------------------------------------------------------------------------
# NOTE :- Here we can use this method also from sklearn.

from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

clf.fit(features_train, labels_train)

clf.score(features_test,labels_test) # 0.9827709978463748

clf.predict(emails)
# array(['ham', 'spam'], dtype='<U4')










