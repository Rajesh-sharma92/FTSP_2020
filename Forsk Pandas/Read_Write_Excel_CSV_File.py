# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:31:53 2020

@author: Rajesh
"""
Reading & Writing CSV File :-
--------------------------
1) Read CSV 
2) Write CSV
3) Read Excel
4) Write Excel
-------------------------------------------------------------------------------------------------------------------
1) Read CSV :- 
   --------
   import pandas as pd
   
   df = pd.read_csv('E:\Forsk Pandas\stock_data.csv')
   #df = pd.read_csv('E:\Forsk Pandas\stock_data.csv' , header = 1) # skiprows = 1
   print(df)

NOTE :- Whenever you have header missing in the data then we need to use all these things into reading csv files.

import pandas as pd
   
   df = pd.read_csv('E:\Forsk Pandas\stock_data.csv' , header = None)
   df = pd.read_csv('E:\Forsk Pandas\stock_data.csv' , header = None, names = ['tickers','eps','revenue','price','people'] ) # skiprows = 1
   print(df)

Question :- Read first 3 rows from dataFrames into csv file.
Answer :- 
import pandas as pd
df = pd.read_csv('E:\Forsk Pandas\stock_data.csv' , nrows = 3)
print(df)
-------------------------------------------------------------------------------------------------------
Question :- How to replace the not available or n.a. columns.
Answer :- 
import pandas as pd
df = pd.read_csv('E:\Forsk Pandas\stock_data.csv' , na_values = ['not available','n.a.'])
print(df)
NOTE :- It will be helping us to cleaning of the messy data.
---------------------------------------------------------------------------------------------------
Question :- How to replace the revenue of one company is -1 in a columan and change it to by Nan.
NOTE :- one more thing we should know that any company revenue can't be in -ve form. So, we should make it Nan.
NOTE :- eps may be -1 or -ve and that should not be change like Nan while replacing value for revenue.

import pandas as pd
df = pd.read_csv('E:\Forsk Pandas\stock_data.csv' , na_values = {
        'eps' : ['not available','n.a.'],
        'revenue' : ['not available','n.a.' , -1],
        'people' : ['not available','n.a.']
        })
print(df)
-------------------------------------------------------------------------------------------------
Question :- How to save into csv file any file ?
Answer :- First we read and got the output into a file then we will be saving that output into another csv file.

df_new = df.to_csv('New_Stock_Data.csv') # Here you will be getting Index also. If you want u can remove also by using just use the index = False.
print(df_new)

Question :- How to remove the index from New_Stock_Data.csv file.
Answer :-  we just need to use the index = False in the dataFrame.

df_new = df.to_csv('New_Stock_Data.csv' , index = False)
print(df_new)
--------------------------------------------------------------------------------------------------
Question :- How to read the particular columan into csv file.
Answer :- we just need to pass the columan Name into file while reading the csv file.
First we will checking all column Names and then select some cols.

df.columns # It shows the Columan Names.
Result = ['tickers', 'eps', 'revenue', 'price', 'people']

df_new = df.to_csv('New_Stock_Data.csv' , columns = ['tickers','eps'] , index = False)
print(df_new)

Question :- If you want to remove the header from new csv file then how is it ?
Answer :- We just need to pass the header = False while reading or writing a  csv file.

df_new = df.to_csv('New_Stock_Data.csv' , header = False)
print(df_new)
------------------------------------------------------------------------------------------------------

Reading & Writing the Excel File :- First we need to create a Excel file with xlsx extension.
--------------------------------
import pandas as pd
   
df = pd.read_excel('E:\Forsk Pandas\stock_data.xlsx' , 'Sheet1')
print(df)
-------------------------------------------------------------------------------------------
Question :- We have a excel sheet and we just want to replace with name 'sam walton' in people col.
Answer :- First we need to create a function and then we will be using converters in file while reading excel file.
NOTE :- Converters always takes value into python dictionary form.
NOTE :- Converters concept is very useful to cleaning the messy data into meaningful data & very Analysis data.

import pandas as pd

def convert_people_cell(cell): # define a function
    if cell == 'n.a.':
        return 'sam walton'
    return cell

def convert_eps_cell(cell):
    if cell == 'not available':
        return None
    return cell

df = pd.read_excel('E:\Forsk Pandas\stock_data.xlsx' , 'Sheet1' , converters = {
        'people' : convert_people_cell, # vale into dict form.
        'eps' : convert_eps_cell # vale into dict form.
        })

print(df)    
--------------------------------------------------------------------------------------------------------
How to write data into Excel file :-
---------------------------------
Question :- How to write data into Excel file ?
Answer :- we just need to use the function which is " to_excel('filename' , 'sheet_name') ".

import pandas as pd

df = pd.read_excel('E:\Forsk Pandas\stock_data.xlsx' , 'Sheet1')
print(df)

df_exl = df.to_excel('New_stock_data.xlsx' , sheet_name = 'stocks')
print(df_exl)

---------------------------------------------------------------------------------------------------
Question :- How to start from particular row & cols into excel file.
Answer :- while reading csv file we can give the as required values like. "startrow = m , startcol = n"

df_exl = df.to_excel('New_stock_data.xlsx' , sheet_name = 'stocks' , startrow = 1 , startcol = 2 , index = False)
print(df_exl)
------------------------------------------------------------------------------------------------------
How to Read multiple Data Frames into a single Excel file :-
---------------------------------------------------------
Question :- How to Read multiple Data Frames into a single Excel file ?
Answer :- By using the class ExcelWriter and reading multiple files into Excel file.

import pandas as pd

df_stocks = pd.DataFrame({'tickers' : ['GOOGLE','WMT','MSFT'],
              'price' : [845,65,64]
             })
df_whether = pd.DataFrame({'day' : ['25/01/20' , '30/03/19'],
            'temp' : [25,40],
            'event' : ['Rain','snow']
        })

with pd.ExcelWriter('stocks_wheather.xlsx') as writer:
    df_stocks.to_excel(writer , sheet_name = 'stocks' , index = False)
    df_whether.to_excel(writer , sheet_name = 'weather' , index = False)
    
    


    






























       

























