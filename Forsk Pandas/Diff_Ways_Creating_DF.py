# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:27:43 2020

@author: Rajesh
"""

There are many ways to create the DataFrames by using Pandas :-
------------------------------------------------------------
1) Using CSV
2) Using Excel
3) From python dictionary
4) From list of tuples
5) From list of dictionaries
-------------------------------------------------------------------------------------
1) Using CSV :-
   ---------
   import pandas as pd
   df = pd.read_csv('E:\Forsk Pandas\Wheater_Data.csv')
   print(df)
   
   ****** Result *********
     day  temperature  windspeed          event
0  2/20/2020           32           6         sunny
1  2/21/2020           34           7          Rain
2  2/22/2020           50           8        shadow
3  2/25/2020           45           2         cloud
4  2/27/2020           38           4  partly cloud
5  2/29/2020           25           9          Rain

------------------------------------------------------------------------------------------
2) Using Excel :-   
   -----------
   import pandas as pd
   df = pd.read_excel('E:\Forsk Pandas\Wheather_Data.xlsx', 'Sheet1')
   print(df)
   ****** Result *********
           day  temperature  windspeed          event
0 2020-02-20           32           6         sunny
1 2020-02-21           34           7          Rain
2 2020-02-22           50           8        shadow
3 2020-02-25           45           2         cloud
4 2020-02-27           38           4  partly cloud
5 2020-02-29           25           9          Rain
   
   
---------------------------------------------------------------------------------------------------
3) From python dictionary :- 
   ----------------------
import pandas as pd
   
Wheater_Data = {'day' : ['2/20/2020','2/21/2020','2/22/2020','2/25/2020','2/27/2020','2/29/2020'],
                'temperature' : [32,34,50,45,38,25],
                'windspeed' : [6,7,8,2,4,9],
                 'event' : ['sunny','Rain','shadow','cloud','partly cloud','Rain']
                }

df = pd.DataFrame(Wheater_Data)
print(df)
   ****** Result *********
        day  temperature  windspeed         event
0  2/20/2020           32          6         sunny
1  2/21/2020           34          7          Rain
2  2/22/2020           50          8        shadow
3  2/25/2020           45          2         cloud
4  2/27/2020           38          4  partly cloud
5  2/29/2020           25          9          Rain

-----------------------------------------------------------------------------------------------------------
4) From list of tuples :-
   -------------------
   import pandas as pd
   
   Wheater_Data = [('2/20/2020',32,6,'sunny'),
                   ('2/21/2020',34,7,'Rain'),
                   ('2/22/2020',50,8,'shadow')]
   
   df = pd.DataFrame(Wheater_Data)
   print(df)
   
   ****** Result *********
             0   1  2   3
0  2/20/2020  32  6   sunny
1  2/21/2020  34  7    Rain
2  2/22/2020  50  8  shadow

df = pd.DataFrame(Wheater_Data , columns = ['day','temperature','windspeed','event'])
print(df)

         day  temperature  windspeed   event
0  2/20/2020           32          6   sunny
1  2/21/2020           34          7    Rain
2  2/22/2020           50          8  shadow
-------------------------------------------------------------------------------------------------------------------
5) From list of dictionaries :-    
   -------------------------
   import pandas as pd
   
   Wheater_Data = [{'day':'2/20/2020','Temp':32,'windspeed':6,'event':'sunny'},
                   {'day':'2/21/2020','Temp':34,'windspeed':7,'event':'Rain'},
                   {'day':'2/22/2020','Temp':50,'windspeed':8,'event':'shadow'}]
   
   df = pd.DataFrame(Wheater_Data)
   print(df)
   
   ****** Result *********
   
            day  Temp  windspeed   event
0  2/20/2020    32          6   sunny
1  2/21/2020    34          7    Rain
2  2/22/2020    50          8  shadow
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   























   