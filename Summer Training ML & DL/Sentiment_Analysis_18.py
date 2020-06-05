# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:42:25 2020

@author: Rajesh
"""

import pandas as pd
import numpy as np 


dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Restaurant_Reviews.tsv' , delimiter = '\t')

dataset.head()
*****************
                                             Review  Liked
0                           Wow... Loved this place.      1
1                                 Crust is not good.      0
2          Not tasty and the texture was just nasty.      0
3  Stopped by during the late May bank holiday of...      1
4  The selection on the menu was great and so wer...      1

# Import nltk Library
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


# For stemming we just need to create the object of PorterStemmer class
from nltk.stem.porter import PorterStemmer

# how to select the first Review for just Testing.
import re
print(dataset['Review'][0]) # Wow... Loved this place.

review = re.sub('[^a-zA-Z]' , ' ' , dataset['Review'][0])
print(review) # Wow    Loved this place 

review = review.lower()
print(review) # wow    loved this place 

review = review.split()
print(review) # ['wow', 'loved', 'this', 'place']

review = [word for word in review
          if not word in set(stopwords.words('english'))]

print(review)  # ['wow', 'loved', 'place'] # Now 'this' is not there into sentance.

# Now we will be creating object for PorterStemmer class
ps = PorterStemmer()

review = [ps.stem(word) for word in review]
print(review) # ['wow', 'love', 'place'] # Means loved = love

review = ' '.join(review)
print(review) # wowloveplace


# Now we will be doing for the Entire dataset.
# Add this into Bigger List.

corpus = []

for i in range(0,1000):
    review = re.sub('[^a-zA-Z]',' ' , dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)
    
    
print(corpus)
print(len(corpus)) # 1000

# Now We will be performing the Vectorzation. It is also called as Features Extraction.
# Bag of words # BOG.

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)

# It is also called as Sparse Matrix for ND array.
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:,1].values


from sklearn.model_selection import train_test_split

features_train , features_test , labels_train , labels_test =\
train_test_split(features,labels,test_size=0.20,random_state=41)


# Now Applying KNN to this dataset.
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()

classifier.fit(features_train,labels_train)

labels_pred = classifier.predict(features_test)

# Now we will be applying the Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test , labels_pred)

print(cm)
**************
[[69 34]
 [47 50]]

print((69+50)/(69+34+47+50)) # 0.595


# Now we will be going for the Naive Bayes algorithms.
from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()

classifier.fit(features_train,labels_train)

labels_pred = classifier.predict(features_test)

# Now we will be applying the Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test , labels_pred)

print(cm)
************
[[60 43]
 [11 86]]

print((60+86)/(60+43+11+86)) # 0.73





