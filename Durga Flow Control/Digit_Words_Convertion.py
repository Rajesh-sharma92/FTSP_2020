# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:31:01 2020

@author: Rajesh
"""
#### 0 - zero , 1 - one , 2-two ......9-nine we need to print it.

## Version :- 1

num = int(input ('Enter the number from 0 to 9 :'))

if num == 0:
        print('ZERO')
        
elif num == 1:
        print('ONE')
        
elif num == 2:
        print('TWO')
        
elif num == 3:
        print('THREE')
        
elif num == 4:
        print('FOUR')
        
elif num == 5:
        print('FIVE')
        
elif num == 6:
        print('SIX')
        
elif num == 7:
        print('SEVEN')
        
elif num == 8:
        print('EIGHT')
        
elif num == 9:
        print('NINE')
    
else:
    
    print('Pls enter the number from 0 t 9 only')
    
 ## Version :- 2
 
while(True): 
    
    list1 = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
    
    num =input('Enter the digit from 0 to 9 only :')
    
    if not num:
        break
    num = int(num)
    
    print(list1[num])
     
        

   
 ## Version :- 3

while(True):
    words_upto_19 = [' ','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINTEEN']   
    
    words_for_tens = [' ',' ','TWENTY','THIRTY','FOURTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
    
    n = input('Enter a number from 0 to 99 :')
    
    if not n:
        break
    
    n = int(n)
    
    output = ' '
    
    if n==0:
        output = 'ZERO'
        print(output)
            
    elif n<=19:
        output = words_upto_19[n]
        print(output)
            
    elif 20<=n<=99:
        output = words_for_tens[n//10] +' '+ words_upto_19[n%10]
        print(output)
            
    else:
        output = 'Please enter the value from 0 to 99 numbers :'
        
        print(output)
    



        
    
        

