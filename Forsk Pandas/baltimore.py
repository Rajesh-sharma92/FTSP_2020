# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:01:43 2020

@author: Rajesh
"""

"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a int.
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:\Forsk Pandas\CSV files\Baltimore_City_Employee_Salaries_FY2014.csv')
print(df)

df.columns

# remove the dollar signs in the AnnualSalary field and assign it as a int.

df['AnnualSalary'] #Annual salary is in float and we need to convert into int64 format.
"""
0        11310.0
1        53428.0
2        68300.0
3        62000.0
4        43999.0
  
18976    11310.0
18977    11310.0
18978    43999.0
18979    44104.0
18980    53568.0
Name: AnnualSalary, Length: 18981, dtype: float64
"""
df['AnnualSalary'].astype('int64')

"""

0        11310
1        53428
2        68300
3        62000
4        43999
 
18976    11310
18977    11310
18978    43999
18979    44104
18980    53568
Name: AnnualSalary, Length: 18981, dtype: int64
"""
# Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
 #Sort the data and display to show who get the highest salary
  
df[['JobTitle','AnnualSalary']]

df['AnnualSalary'].agg(['sum','mean','std'])

sum     7.546237e+08
mean    3.975679e+04
std     2.517305e+04
Name: AnnualSalary, dtype: float64

# Try to group on JobTitle only and sort the data and display.

df['JobTitle']

df['JobTitle'].unique()

df['JobTitle'].count() # 18981

sort=df['JobTitle']
sorted(sort)

# How many employess are there for each JobRoles and Graph it.

df.columns

df['JobTitle'].value_counts()
df['JobTitle'].unique()

plt.pie(df['JobTitle'].value_counts(),labels=df['JobTitle'].unique(),radius =3 , autopct='%1.2f%%')
plt.savefig('E:\Forsk Pandas\Baltmore.jpg')
plt.show()


df.columns

# Graph and show which Job Title spends the most.

# List All the Agency ID and Agency Name.

df[['AgencyID','Agency']]

      AgencyID                    Agency
0       W02200            Youth Summer  
1       A03031       OED-Employment Dev 
2       A29005  States Attorneys Office 
3       A65026   HLTH-Health Department 
4       A99416        Police Department 
       ...                       ...
18976   W02235            Youth Summer  
18977   W02629             Youth Summer 
18978   A99416        Police Department 
18979   A99262        Police Department 
18980   A50206  DPW-Water & Waste Water 

[18981 rows x 2 columns]


# Find all the missing Gross data in the dataset .
df[df[df.columns].isnull()]

      Name JobTitle AgencyID Agency HireDate  AnnualSalary  GrossPay
0       NaN      NaN      NaN    NaN      NaN           NaN       NaN
1       NaN      NaN      NaN    NaN      NaN           NaN       NaN
2       NaN      NaN      NaN    NaN      NaN           NaN       NaN
3       NaN      NaN      NaN    NaN      NaN           NaN       NaN
4       NaN      NaN      NaN    NaN      NaN           NaN       NaN
    ...      ...      ...    ...      ...           ...       ...
18976   NaN      NaN      NaN    NaN      NaN           NaN       NaN
18977   NaN      NaN      NaN    NaN      NaN           NaN       NaN
18978   NaN      NaN      NaN    NaN      NaN           NaN       NaN
18979   NaN      NaN      NaN    NaN      NaN           NaN       NaN
18980   NaN      NaN      NaN    NaN      NaN           NaN       NaN

[18981 rows x 7 columns]

---------------------------------------------------------------------------------------
plt.figure(figsize= (50,10))
x = df['JobTitle'].unique()
y = df['JobTitle'].value_counts()
plt.bar(x,y)
# simple line plot
plt.plot(x,y)
plt.savefig('E:\Forsk Pandas\Baltmore_Bar.jpg')
plt.show()

























