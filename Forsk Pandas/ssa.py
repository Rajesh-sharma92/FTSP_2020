# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:21:23 2020

@author: Rajesh
"""
"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""


import pandas as pd
list1=range(1880,2018)
list_year=[]
fp=open(r'E:\Forsk Pandas\CSV files\baby_data.csv','a')      
for i in list1:
    f=open(r'E:\Forsk Pandas\CSV files\baby_names\yob'+str(i)+'.txt','r')
    fp.write(f.read())
    f=open(r'E:\Forsk Pandas\CSV files\baby_names\yob'+str(i)+'.txt','r')
    data=f.readlines()
    year=len(data)*[i]
    list_year.extend(year)
    f.close()
fp.close()    
df=pd.read_csv(r'E:\Forsk Pandas\CSV files\baby_data.csv',names=['name','sex','count'])
df['year']=list_year
df