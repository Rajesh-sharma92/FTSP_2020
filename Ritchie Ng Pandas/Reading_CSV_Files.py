import pandas as pd

url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv'

dataset = pd.read_csv(url)

dataset.head()

user_cols = ['FN','LN','Addr','State','City','zip_code']

 dataset = pd.read_csv(url,sep=',',header=None,names=user_cols)
# dataset = pd.read_csv(url,delimiter=',',header=None,names=user_cols)
dataset.head()

dataset.tail()

dataset.info()

dataset.shape # (6, 6)

dataset.size # 36

dataset.index # RangeIndex(start=0, stop=6, step=1)

dataset.columns
----------------------
Index(['FN', 'LN', 'Addr', 'State', 'City', 
       'zip_code'], dtype='object')


dataset.dtypes
--------------
FN          object
LN          object
Addr        object
State       object
City        object
zip_code     int64
dtype: object


dataset.values

dataset.keys

dataset.loc[2:5]

dataset.iloc[2:5]

dataset['FN'].head()

dataset[['LN','Addr']].tail()

dataset['FN'].unique()

dataset['Addr'].unique()

list1 = dataset['zip_code'].unique().tolist()
print(list1) # [8075, 9119, 91234, 298, 123]
print(type(list1))


dataset['Addr'].value_counts()

dataset['FN'].value_counts()

dataset['FN'].value_counts(normalize=True) # It shows value into Percentage.

dataset['zip_code'].value_counts(dropna=False)

dataset['zip_code'].value_counts(dropna=True)

dataset['FN'].count()

dataset['zip_code'].mean() # 19487.3333

dataset['zip_code'].std() # 35380.1558428827

dataset['zip_code'].describe() # 

dataset['zip_code'].min() # 123

dataset['zip_code'].max() # 91234

count        6.000000
mean     19487.333333
std      35380.155843
min        123.000000
25%       2242.250000
50%       8075.000000
75%       8858.000000
max      91234.000000
Name: zip_code, dtype: float64

dataset['zip_code'].isnull()

dataset[dataset['zip_code'].isnull()]


df_age = df.groupby(['age'])
df_age.size() # 61

df_age.count() # 61

df_age.groups

df_ocu = df.groupby(['occupation'])

df_ocu.groups['technician']

df_ocu.groups['writer']




