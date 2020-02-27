# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:46:56 2020

@author: Rajesh
"""
"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""


import pandas as pd

df = pd.read_csv(r'E:\Forsk Pandas\CSV files\training_titanic1.csv')

-->> How many people in the given training set survived the disaster ?

df[df['Survived'] == 1].count() # 342

--->> How many people in the given training set died ?

df[df['Survived'] == 0].count() # 549      

--->> Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      
df['Survived'].value_counts(normalize = True)
df['Survived'].value_counts(normalize = False)        

-->> Males that survived vs males that passed away.

df[(df['Survived'] == 1) & (df['Sex']=='male')] # 109
df[(df['Survived'] == 0) & (df['Sex']=='male')] # 468


-->> Females that survived vs Females that passed away.

df[(df['Survived'] == 1) & (df['Sex']=='female')] # 233
df[(df['Survived'] == 0) & (df['Sex']=='female')] # 81                  
   
df[df['Age']<=18]   # childrens = 139

df[(df['Survived'] == 1) & (df['Age']<=18)] # Survive Chdild : 70

df[df['Age']<=18]   # childrens = 139

df[(df['Survived'] == 0) & (df['Age']<=18)] # Survive Chdild : 69

df['Ischild']=df['Age'].map(lambda x: 1 if x <=18 else 0)

# How many childrens are surived & died below 18 & after 18 years.

df["Ischild"].value_counts(normalize = True)*100

0    84.399551
1    15.600449

------------------------------------------------------------------------------------------------------

# Make a pie chart of how many people have survived & Died ?.

import matplotlib.pyplot as plt

labels = ['Survived' , 'Died']
sizes = [342 , 549]
colors = ['Red','Blue']
explode = (0.1,0)
plt.title('Total survived & Died')

plt.pie(sizes ,labels = labels , colors = colors , explode = explode , autopct='%1.2f%%' ,shadow = True , startangle = 90)
plt.axis('equal')
# plt.savefig('')
plt.show()
  
-----------------------------------------------------------------------------------------------------------------
# Make a pie chart of how many Male have survived & Died ?.

import matplotlib.pyplot as plt

labels = ['Survived' , 'Died']
sizes = [109 , 468]
colors = ['Green','skyBlue']
explode = (0,0.3)
plt.title('Total Male survived & Died')

plt.pie(sizes ,labels = labels , colors = colors , explode = explode , autopct='%1.2f%%' ,shadow = True , startangle = 90)
plt.axis('equal')
# plt.savefig('')
plt.show()
---------------------------------------------------------------------------------------------------
# Make a pie chart of how many Female have survived & Died ?.

import matplotlib.pyplot as plt

labels = ['Survived' , 'Died']
sizes = [233, 81]
colors = ['Red','skyBlue']
explode = (0,0.1)
plt.title('Total Female survived & Died')

plt.pie(sizes ,labels = labels , colors = colors , explode = explode , autopct='%1.2f%%' ,shadow = True , startangle = 90)
plt.axis('equal')
# plt.savefig('')
plt.show()
------------------------------------------------------------------------------------------------------------------
# Make a pie chart of how many Childrens  have survived & Died ?.

import matplotlib.pyplot as plt

labels = ['Survived' , 'Died']
sizes = [70, 69]
colors = ['lightGreen','Blue']
explode = (0,0.1)
plt.title('Total Childrens survived & Died')

plt.pie(sizes ,labels = labels , colors = colors , explode = explode , autopct='%1.2f%%' ,shadow = True , startangle = 270)
plt.axis('equal')
# plt.savefig('')
plt.show()
-----------------------------------------------------------------------------------------------------
# How many childrens are surived & died below 18 & after 18 years.

import matplotlib.pyplot as plt

labels = ['After 18 yrs','below 18 yrs']
sizes = [84, 15]
colors = ['lightGreen','Blue']
explode = (0,0.3)
plt.title('Total Childrens survived & Died as per ')

plt.pie(sizes ,labels = labels , colors = colors , explode = explode , autopct='%1.2f%%' ,shadow = True , startangle = 270)
plt.axis('equal')
# plt.savefig('')
plt.show()









































