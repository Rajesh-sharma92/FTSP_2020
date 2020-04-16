# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:11:51 2020

@author: Rajesh
"""
"""
Our Classification Algorithm only understand number

How to convert the textual data into numbers ?
NLP Steps
    1. Noise Removal / Stopword Removal 
    2. Lexicon Normalization - Stemming
    3. Vectorisation / Bag of Words Model
    4. Creation of Machine Learning Model 

Step 1: Noise Removal / Stopword Removal / Clean Up Process
        this is good     ---> positive 
        good             ---> positive  ( removal of this and is stopwords)

        Stopwords removing = remove articles from the sentense does not 
                             change the sentiments of the statement      

Step 2: Stemming is the process to find the root form of word ( first form )
        hated, hating, loving, loved
        hate and love
        
Step 3: Vectorisation
        Convert text data to numeric form
        We would label Encode and then OneHotEncoding
        
Step 4: ML - classification to build the model        
"""
# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Restaurant_Reviews.tsv',delimiter='\t')

# Cleaning the texts
# Noise removal
""" language stopwords 
(commonly used words of a language – is, am, the, of, in etc), 
URLs or links, social media entities (mentions, hashtags), 
punctuations and industry specific words. 
This step deals with removal of all types of noisy entities present in the text.
"""
# !pip install nltk # We need to install the nltk for the first time.
import nltk

# download the latest list of stopwords from Standford Server 
nltk.download('stopwords')

from nltk.corpus import stopwords

"""
The most common lexicon normalization practices are :

Stemming:  Stemming is a rudimentary rule-based process of stripping the 
suffixes (“ing”, “ly”, “es”, “s” etc) from a word.

Lemmatization: Lemmatization, on the other hand, is an organized 
& step by step procedure of obtaining the root form of 
the word, it makes use of vocabulary (dictionary importance of words) 
and morphological analysis (word structure and grammar relations).
"""
#For Stemming use the PorterStemmer class object 
from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer 

"""
Apply the process to one line of text
This will help in understanding the below logic
"""
# perform row wise noise removal and stemming
# let's do it on just first row data
# Wow... Loved this place.    1

import re # RegEx means Regular Experession.
print(dataset['Review'][0]) # Wow... Loved this place.

"""
Search through regex for special character set , using the substitute function 
substitute the regex with space ' ' 
[^a-zA-Z ] finds those which does not belong to a to z or A to Z
"""
review= re.sub('[^a-zA-Z]',' ',dataset['Review'][0])
print(review) # Wow    Loved this place 

review = review.lower()
print(review) # wow    loved this place 

review = review.split()
print(review) # ['wow', 'loved', 'this', 'place']

# We need to check whether it is a stopword, if YES then remove it

review = [ word for word in review
 if not word in set(stopwords.words('english')) ]

print(review) # ['wow', 'loved', 'place']

# lem = WordNetLemmatizer() # Another way of finding root word
ps = PorterStemmer()
review = [ ps.stem(word) for word in review ]

print(review) # ['wow', 'love', 'place']

review = ' '.join(review)
print(review) # wow love place

# Now do the same for every row in dataset. run to loop for all rows
# Add into this bigger list

corpus = []

for i in range(0,1000):
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review = review.lower()
    review = review.split()
    
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    ps = PorterStemmer()
    review = [ ps.stem(word) for word in review ]
    
    review = ' '.join(review)
    
    corpus.append(review)
    
print(corpus)
# ['wast enough life pour salt wound draw time took bring check']

print(len(corpus)) # 1000
    
# Creating the Bag of Words model
# Also known as the vector space model
# Text to Features (Feature Engineering on text data)
# Conversion of text to Numeric data is known as Feature Extraction 
"""
Rahul   -   nice place
Nitish  -   good one
Ravi    -   awesome

How to convert the above into numneric form ?

New column are created for each unique word

Then it applies a logic similar to OneHotEncoding, but in Onehot there use to 
be one 1 in each row
If good comes twice then it will come twice in the column

nice    place   good    one     awesome
1        1        0      0        0
0        0        1      1        0
0        0        0      0        1

This process is known as Vectorisation of your text
This concept is known as Bag of Words model in NLP

There are other ways to convert text to numerical ways
    1. Bag of Words 
    2. TF-IDF ( compressed way, does not create too much columns )
    3. Word Embedding ( used in Deep Learning)
"""  
"""
internally it creates a dictionary of unique words with values as the count
{
"nice" : 1,
"place" : 1,
"good" : 1,
"one" : 1,
"awesome" : 1
}
top 1500 unique needs to be taken
"""
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
# it is known as sparse matrix of the features ND Array.

features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:,1].values

print(features.shape) # (1000, 1500)

print(labels.shape) # (1000,)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size = 0.20, random_state = 0)

#applying knn on this text dataset
# Fitting Knn to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)
print(cm_knn) 
-----
[[74 23]
 [55 48]]

print((74+48)/(74+23+55+48)) # 0.61


# for better NLP results we need lot of data
# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train,labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
------
[[55 42]
 [12 91]]

print((55+91)/(55+42+12+91)) # 0.73

'''
NOTE :- 
# for better NLP results we need lot of data
# How to predict for a new data ?
# We need to follow the same steps and create the sparse matrix for it 
# only transform and not fit_transform 
'''

