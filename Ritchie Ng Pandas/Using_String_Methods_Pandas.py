# Using String Methods in Pandas :- 

# convert string to uppercase in Python

s1 = 'hello'.upper()

print(s1) # 'HELLO'


Q.1. How about string methods in pandas?
Answer :- There are many!

import pandas as pd

url = 'http://bit.ly/chiporders'

df = pd.read_csv(url , delimiter = '\t')

df.head()

df.columns
--------------
Index(['order_id', 'quantity', 'item_name', 'choice_description',
       'item_price'], dtype='object')


df['item_name'].head()
-----------------
0             Chips and Fresh Tomato Salsa
1                                     Izze
2                         Nantucket Nectar
3    Chips and Tomatillo-Green Chili Salsa
4                             Chicken Bowl
Name: item_name, dtype: object



# Making the item_name uppercase.

df['item_name'].str.upper().head()
------------------------
0             CHIPS AND FRESH TOMATO SALSA
1                                     IZZE
2                         NANTUCKET NECTAR
3    CHIPS AND TOMATILLO-GREEN CHILI SALSA
4                             CHICKEN BOWL
Name: item_name, dtype: object


# you can overwrite with the following code.
df['item_name'] = df['item_name'].str.upper().head()

df['item_name']

df['item_name'].head(10)


# Check presence of substring
# This is useful to filter data

df['item_name'].str.contains('Chicken').head()
---------------
0    False
1    False
2    False
3    False
4     True
Name: item_name, dtype: bool


# Chain string methods
# replacing elements

df['choice_description'].head()
---------------------
0                                                  NaN
1                                         [Clementine]
2                                              [Apple]
3                                                  NaN
4    [Tomatillo-Red Chili Salsa (Hot), [Black Beans...
Name: choice_description, dtype: object


df['choice_description'].str.replace('[' , '').head()
--------------------------
0                                                  NaN
1                                          Clementine]
2                                               Apple]
3                                                  NaN
4    Tomatillo-Red Chili Salsa (Hot), Black Beans, ...
Name: choice_description, dtype: object



# chain string methods.
df['choice_description'].str.replace('[' , '').str.replace(']','').head()
----------------------------
0                                                  NaN
1                                           Clementine
2                                                Apple
3                                                  NaN
4    Tomatillo-Red Chili Salsa (Hot), Black Beans, ...
Name: choice_description, dtype: object



# Using regex to simplify the code above.

df['choice_description'].str.replace('[\[\]]' , '').head()
--------------------
0                                                  NaN
1                                           Clementine
2                                                Apple
3                                                  NaN
4    Tomatillo-Red Chili Salsa (Hot), Black Beans, ...
Name: choice_description, dtype: object


df.columns

df['item_price'].head()
--------------------
0     $2.39 
1     $3.39 
2     $3.39 
3     $2.39 
4    $16.98 
Name: item_price, dtype: object


# Remove the $ and Put INR Symobl.

df['item_price'].str.replace('$' , 'INR ').head()
-----------------
0     INR 2.39 
1     INR 3.39 
2     INR 3.39 
3     INR 2.39 
4    INR 16.98 
Name: item_price, dtype: object


df['quantity'].head()

for qty in df['quantity'].head():
    print(qty)

1
1
1
1
2

for index,qty in df['quantity'].items():
    print(index,qty)

df.count()['quantity'] # 4622


------------------------------------------------------------------

list1 = [10,20,30,40,50,'Rajesh','forsk']

for i in list1:
    print(i)




