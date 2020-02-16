# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:20:28 2020

@author: Rajesh
"""
""" Pg (1) : We just need to perform the banking daily basis transactions like 
amount deposit & amt withdraw. """
-----------------------------------------------------------------------------

import sys
class customer:
    ''' Customer class with banking related operations '''
    
    bankname = 'FORSK CODING SCHOOL BANK' # Static variable.
    
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self,amt):
        self.balance = self.balance+amt
        print('After deposit the balance :', self.balance)
        
    def withdraw(self,amt):
        if amt > self.balance:
            print('Insufficient fund .... can not perform operation this operation')
            sys.exit()
            #else:
        self.balance = self.balance - amt
        print('After withdraw the balance :', self.balance)
print('Welcome to ', customer.bankname)
name = input('Enter your name :')
c = customer(name)

while(True):
    
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option = input('Choose your option :')
    
    if option =='d' or option =='D':
        amt = float(input('Enter the amount to deposit :'))
        c.deposit(amt)
        
    elif option =='w' or option =='W':
        amt = float(input('Enter the amount to withdraw :'))
        c.withdraw(amt)
        
    elif option =='e' or option =='E':
        print('****** Thanks for banking with us *****')
        sys.exit()
    
    else:
        
        print('Choose valid option to perfrom any operations')
    
                
                
                
                
                
                
                
                
                
                
                
                
                
    

