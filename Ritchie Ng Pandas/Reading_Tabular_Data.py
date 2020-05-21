# Pandas :- is nothing but the Panel data set.

# What are Pandas ?
# Pandas is Open-Source Data Analysis Library.
# It provides the functionalites for easy to use data-structures & 
# Data Analysis tools.

''' Benefits of Pandas '''
i) A lots of functionalities.
ii) Active Community.
iii) Extensive Documentation
iv) Plays well with other Packages.
a) Built on top of NumPy
b) Works well with Scikit-learn (Sklearn)

# How to import the pandas and doing Aliasing for Pandas.

import pandas as pd

url = 'http://bit.ly/chiporders'

orders = pd.read_table(url)

orders.head()

# read_table assumptions
# file is separated by tabs
# presence of a header role

url1 = 'http://bit.ly/movieusers'
users = pd.read_table(url1)
users.head()

'''
Issues

Separator is a pipe character
We need to tell pandas that this is the separator using sep=
There is no header
We need to use header=None
We can add a row of names for the columns using names=user_cols
'''

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
df = pd.read_table(url1,sep='|',header=None,names= user_cols)
df.head()
----------------------------
   user_id  age gender  occupation zip_code
0        1   24      M  technician    85711
1        2   53      F       other    94043
2        3   23      M      writer    32067
3        4   24      M  technician    43537
4        5   33      F       other    15213

df.head(10)


df = pd.read_table(url1,sep='|',header=None,names= user_cols)

'''
Tips
If you've a data file where you've some text at the top and bottom of the file
skiprows=None
Skip rows at the top or bottom
skipfooter=None
'''

df.info()

df.size # 4715

df.shape # (943, 5)

df.dtypes
---------------
user_id        int64
age            int64
gender        object
occupation    object
zip_code      object

df.head() # It shows First 5 records from df.

df.tail() # It shows Last 5 records from df.

df.index # RangeIndex(start=0, stop=943, step=1)

df.columns # It will show all columns Name from df.

df.values # It show the all values presented into df.

df.keys # It show the all values presented into df with ColumNames.

df.loc[0:5] # It is included last value as a Index.
-------------
   user_id  age gender  occupation zip_code
0        1   24      M  technician    85711
1        2   53      F       other    94043
2        3   23      M      writer    32067
3        4   24      M  technician    43537
4        5   33      F       other    15213
5        6   42      M   executive    98101

df.iloc[0:5]  # Doesn't included last value as a Index.
-----------------
  user_id  age gender  occupation zip_code
0        1   24      M  technician    85711
1        2   53      F       other    94043
2        3   23      M      writer    32067
3        4   24      M  technician    43537
4        5   33      F       other    15213

df['gender'].head()
df['user_id'].tail()

df[['user_id','age']].head() # It show the UserID & Age first 5 rows.
 
df[['user_id','occupation']].tail() # It show the UserID & Age last 5 rows.

df['age'].unique()

df['occupation'].unique()

list1 = df['user_id'].unique().tolist()
print(type(list1))
print(list1)

df['user_id'].value_counts()

df['user_id'].value_counts(normalize=True)

df['age'].value_counts(dropna=False).head()
df['age'].value_counts(dropna=True).head()

df['age'].count() # 943
df['age'].min() # 7
df['age'].max() # 73
df['age'].mean() # 34.05196182396607
df['age'].std() # 12.192739733059044

df['age'].describe()
---------------------------
count    943.000000
mean      34.051962
std       12.192740
min        7.000000
25%       25.000000
50%       31.000000
75%       43.000000
max       73.000000
Name: age, dtype: float64

df['age'].isnull() # If No Null means it will only False.
df['zip_code'].isnull()






