import pandas as pd

df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

df.head()

df.tail()

df.info()

df.shape # (78, 6)

df.size # 468

df.ndim # 2

df.dtypes # It shows data types of all different columns.

df.index # RangeIndex(start=0, stop=78, step=1)

df.columns
---------------
Index(['rank', 'discipline', 'phd', 'service', 'sex', 
       'salary'], dtype='object')

df.values # numpyrepresentation of the data

"""
Data Frames: method loc

If we need to select a range of rows, using their labels/index 
we can use method loc
"""

df.loc[1:3] # It will work 

df.loc[:5,['rank','sex','salary']] # It will work 

"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""

df.iloc[1:3] # It will work 

df.iloc[3:10 , [4,5,0]]

df[['rank','salary']].head()
---------------------
   rank    salary
0  Prof  186960.0
1  Prof   93000.0
2  Prof  110515.0
3  Prof  131205.0
4  Prof  104800.0

# Find unique values in a Series / Column.
df['rank'].unique()
df['sex'].unique()
df['discipline'].unique()

list1 = df['rank'].unique().tolist()
print(type(list1))
print(list1) # ['Prof', 'AssocProf', 'AsstProf']


df['rank']

df['rank'].value_counts()
-----------------------
Prof         46
AsstProf     19
AssocProf    13
Name: rank, dtype: int64

# to show in Percentage 
df['rank'].value_counts(normalize = True)


df['sex']
df['sex'].value_counts()
--------------------
Female    39
Male      39
Name: sex, dtype: int64

df['sex'].value_counts(normalize=True)
------------------------
Female    0.5
Male      0.5
Name: sex, dtype: float64


# count missing values 
# ( It also counts the NaN Values in the Series/Column).

df.isnull().head(10)

df['sex'].value_counts(dropna=False)
--------------------
Female    39
Male      39
Name: sex, dtype: int64

df['phd'].value_counts()
df['phd'].value_counts(dropna=False)

df['discipline'].value_counts(dropna=False)
-----------------
B    42
A    36
Name: discipline, dtype: int64

df['salary'].value_counts()
df['salary'].value_counts(dropna=False)

# Find how many values in the salary column which are non NaN (use count method).
df['salary'].count() # 76

df['phd'].count() # 76

df['rank'].count() # 78

# Boolean Indexing
# Find those rows which has null values in salary/phd column
df['salary'].isnull() # 78
df[ df['salary'].isnull() ]
----------------------
        rank discipline   phd  service   sex  salary
7       Prof          A  18.0       18  Male     NaN
28  AsstProf          B   7.0        2  Male     NaN

df['phd'].isnull()
df[ df['phd'].isnull() ]
-------------------------------
         rank discipline  phd  service   sex    salary
13       Prof          B  NaN       33  Male  162200.0
34  AssocProf          B  NaN        8  Male  119800.0

df['rank'].isnull()
df[ df['rank'].isnull() ]

"""
Data Frames groupby method

Using "group by" method we can:
Split the data into groups based on some criteria
Calculate statistics (or apply a function) to each group
"""
# Group data using rank.
df_rank = df.groupby(['rank'])

df_rank.size()
------------------
rank
AssocProf    13
AsstProf     19
Prof         46
dtype: int64

df_rank.count()
--------------------
           discipline  phd  service  sex  salary
rank                                            
AssocProf          13   12       13   13      13
AsstProf           19   19       19   19      18
Prof               46   45       46   46      45

df_rank.groups

# Groups returns a dictionary object.
df_rank.groups['AssocProf']
df_rank.groups['AsstProf']
df_rank.groups['Prof']

df_rank.groups['AsstProf'][2:5] # [17, 20, 22]
df_rank.groups['Prof'][9] # 10
df_rank.groups['Prof'][:5]


# group data using rank followed  by discipline and sex
df_rank=df.groupby(['rank', 'discipline','sex'])
df_rank.groups
df_rank.count()


df_disp = df.groupby(['discipline','sex','salary'])
df_disp.groups
df_disp.count()

# Calculate mean value for each numeric column per each group
df_rank.mean()

# Calculate mean salary for each type of professor rank:
df.groupby('rank')['salary','phd'].min()
------------------
           salary   phd
rank                    
AssocProf  62884.0   9.0
AsstProf   63100.0   1.0
Prof       57800.0  12.0

df.groupby('rank')['salary','phd'].max()
---------------
             salary   phd
rank                     
AssocProf  119800.0  26.0
AsstProf    97032.0  11.0
Prof       186960.0  56.0

df.groupby('rank')['salary','phd'].mean()
----------------------
                  salary        phd
rank                               
AssocProf   91786.230769  15.333333
AsstProf    80810.722222   5.052632
Prof       123565.355556  26.888889

df.groupby('rank')['salary','phd'].std()
------------------
                salary        phd
rank                              
AssocProf  18571.183714   5.757735
AsstProf    9330.234155   2.738079
Prof       25127.782785  10.229685

df.groupby('rank')['salary','phd'].describe() # It will work

"""
Data Frame: filtering

To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:

"""
# Boolean Indexing in Pandas
# select only those professors who has salary more than 120000

df['salary'] > 120000
df_sub = df[ df['salary'] > 120000 ]
df_sub
df_sub.count()

# to display only the selected series/column
df.loc[df['salary'] > 120000,'salary']

# filter using multiple columns.
df_sub = df [ (df['salary'] > 120000) & \
(df['phd'] > 10)  & \
(df['sex'] == 'Female') ]

df_sub

df_sub = df [ (df['salary'] > 120000) & \
             (df['phd'] > 10)  & \
             (df['sex'] == 'Female') &\
             (df['discipline'] == 'A') ]

df_sub
---------
    rank discipline   phd  service     sex    salary
40  Prof          A  39.0       36  Female  137000.0

df_sub = df [ (df['salary'] > 160000) &\
             (df['sex'] == 'Male') ]

df_sub
-----------
    rank discipline   phd  service   sex    salary
0   Prof          B  56.0       49  Male  186960.0
13  Prof          B   NaN       33  Male  162200.0

df_sub.count()


"""
Missing Values
"""
df.info()

df[df['phd'].isnull()]
------------------
         rank discipline  phd  service   sex    salary
13       Prof          B  NaN       33  Male  162200.0
34  AssocProf          B  NaN        8  Male  119800.0

df[df['salary'].isnull()]
---------------
        rank discipline   phd  service   sex  salary
7       Prof          A  18.0       18  Male     NaN
28  AsstProf          B   7.0        2  Male     NaN

'''How to fix missing values'''

df['discipline'].isnull().count() # 78

new_df2 = df.fillna(0)

new_df2

new_df2.count()

df.count()

# NOTE :- To make the changes into Acutal data frames. Inplace = True

df.fillna(0,inplace=True)

df.count() # Now, It's working.

# Fill All columns with missing values, with mean of that column
mean = df.mean()
df = df.fillna(round(mean,0))
df.head(10)

# fill all the records with missing values, with mean of that column.
df['phd'] = df['phd'].fillna(df['phd'].mean())

df['phd']

df[df['phd'].isnull()]

# fill all the records with missing values, with mean of that column.
df['salary'] = df['salary'].fillna(df['salary'].median())

df['salary']

df[ df['salary'].isnull() ]


''' How to drop columns '''
df.drop('discipline',axis=1 , inplace = True)
df.count() # We have dropped the discipline column from DataFrame.

df1 = df.dropna()
df1.count()

# Creating a new Column based on some other columns values 
# Male == 0 and Female == 1
df['sex_bool'] = df['sex'].map(lambda x : 0 if x== 'Male' else 1)
df['sex_bool']

df.count()
df.columns


# Value Conversion using apply function 
# Male == 0 and Female == 1

df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

df.head(2)
-----------
   rank discipline   phd  service   sex    salary
0  Prof          B  56.0       49  Male  186960.0
1  Prof          A  12.0        6  Male   93000.0


def gender_code(x):
    if x == 'Male':
        return 0 
    elif x == 'Female':
        return 1
    
df['sex'].value_counts(dropna=False)    
-----------
Female    39
Male      39
Name: sex, dtype: int64

df['sex'] = df['sex'].apply(gender_code)    
    
df['sex'].head()
------------
0    0
1    0
2    0
3    0
4    0
Name: sex, dtype: int64

df['sex'].value_counts(dropna=False)    
----------
1    39
0    39
Name: sex, dtype: int64

df.head(2)
-----------
   rank discipline   phd  service  sex    salary
0  Prof          B  56.0       49    0  186960.0
1  Prof          A  12.0        6    0   93000.0

df.tail(2)
----------
    rank discipline   phd  service  sex    salary
76  Prof          A  28.0       14    1  109954.0
77  Prof          A  23.0       15    1  109646.0

df

"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""

import pandas as pd

df = pd.read_csv('E:\PYTHON CODE Challenges\Pandas\Salaries.csv')

Q. 1. Which Male and Female Professor has the highest and the lowest salaries ?
Answer :- 

df[(df['rank'] == 'Prof') & (df['sex'] == 'Male')]['salary'].max() # 186960.0
             

df[(df['rank'] == 'Prof') & (df['sex'] == 'Male')]['salary'].min() # 57800.0
             

df[(df['rank'] == 'Prof') & (df['sex'] == 'Female')]['salary'].max() # 161101.0
             

df[(df['rank'] == 'Prof') & (df['sex'] == 'Female')]['salary'].min() # 90450.0


Q. 2. Which Professor takes the highest and lowest salaries ?
Answer :- 

df[df['rank'] == 'Prof']['salary'].max() # 186960.0

df[df['rank'] == 'Prof']['salary'].min() # 57800.0

df[df['rank'] == 'AssocProf']['salary'].max() # 119800.0
             
df[df['rank'] == 'AssocProf']['salary'].min() # 62884.0

df[df['rank'] == 'AsstProf']['salary'].max() # 97032.0

df[df['rank'] == 'AsstProf']['salary'].min() # 63100.0



Q. 3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same ?
Answer :- 

df[df['salary'].isnull()]
------------------
        rank discipline   phd  service   sex  salary
7       Prof          A  18.0       18  Male     NaN
28  AsstProf          B   7.0        2  Male     NaN

mis_sal = df[df['salary'].isnull()]['service']
   
mis_sal

df [(df['service'] == 18) | (df['service'] == 2)] 

df1 = df[df['service'] == 18]
x = df1['salary'].mean()
print(x) # 119190.0

df2 = df[df['service'] == 2]
y = df2['salary'].mean()
print(y) # 76908.33333333333


df[ df['service'] == 18 ]['salary'].fillna(x)
----------
4     104800.0
7     119190.0
33    120000.0
39    129000.0
49    122960.0
Name: salary, dtype: float64

df [df['service'] == 2 ]['salary'].fillna(y)
--------------
22    73000.000000
28    76908.333333
42    80225.000000
68    77500.000000
Name: salary, dtype: float64


Q. 4. Missing phd - should be mean of the matching service ?
Answer :- 

mis_phd = df[ df['phd'].isnull() ]
mis_phd
------------------
         rank discipline  phd  service   sex    salary
13       Prof          B  NaN       33  Male  162200.0
34  AssocProf          B  NaN        8  Male  119800.0


df [(df['service'] == 33) | (df['service'] == 8)] 

df1 = df[ df['service'] == 33 ]
x = df1['service'].mean()
print(x) # 33.0

df2 = df [ df['service'] == 8 ]
y = df2['service'].mean()
print(y) # 8.0


df[ df['service'] == 33 ]['phd'].fillna(x)
-------------
10    39.0
13    33.0
Name: phd, dtype: float64

df[ df['service'] == 8 ]['phd'].fillna(y)
-------------
34     8.0
37    20.0
41    13.0
56    10.0
Name: phd, dtype: float64

df['phd'].head(35)

df[ df['phd'].isnull() ]


Q. 5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
Answer :- 

df_Male_staff = df[(df['sex'] == 'Male') & (df['rank']) ]

df_Male_staff.count()['sex'] # 39

df_Female_staff = df[(df['sex'] == 'Female') & (df['rank']) ]

df_Female_staff.count()['sex'] # 39

df['sex'].count() # 78


Q. 6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart ?
Answer :- 

df_Prof = df[ df['rank'] == 'Prof' ]

df_Prof.count()['rank'] # 46

df_AssocProf = df[ df['rank'] == 'AssocProf' ]

df_AssocProf.count()['rank'] # 13

df_AsstProf = df[ df['rank'] == 'AsstProf' ]

df_AsstProf.count()['rank'] # 19

df['rank'].count() # 78      # 46+13+19 = 78


Q. 7. Who are the senior and junior most employees in the organization.
Answer :- 

df.head()

df['service'].max() # 51

df['service'].min() # 0


df_emp = df.groupby('rank')[['service']].max()

df_emp
----------
          service
rank              
AssocProf       24
AsstProf         6
Prof            51

df[(df['rank'] == 'AssocProf')]['service'].max() # 24

df[(df['rank'] == 'AsstProf')]['service'].max() # 6

df[(df['rank'] == 'Prof')]['service'].max() # 51


df_emp = df.groupby('rank')[['service']].min()

df_emp
------------
           service
rank              
AssocProf        6
AsstProf         0
Prof             0

df[(df['rank'] == 'AssocProf')]['service'].min() # 6

df[(df['rank'] == 'AsstProf')]['service'].min() # 0

df[(df['rank'] == 'Prof')]['service'].min() # 0







