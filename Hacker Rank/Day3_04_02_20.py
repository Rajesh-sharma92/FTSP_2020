# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:00:31 2020

@author: Rajesh
"""



def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    
    #########################
    
a = "this is a string"

b = a.split(" ") # a is converted to a list of strings. 

print(b)

c= "-".join(b)

print(c)


#####################

def b(a):
    c= a.split()
    d = "-".join(c)
    return d
     


if __name__ == '__main__':
    line = input()
    result = b(line)
    print(result)
    
    
  ######################


def print_full_name(a, b):
    print("Hello" , a , b+"! You just delved into python.")

if __name__ == '__main__':
    
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


##############################
 
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
    
    
    
    
    
    
    
    



  
    
    
    
    