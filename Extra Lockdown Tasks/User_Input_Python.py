# How to Take User Input In Python
Ex :- 
x = 100 # Hard value
y = 200
z = x+y
print('The Sum :',z)

Ex :- 
x = int(input('Enter X value :'))
y = int(input('Enter Y value :'))
z = x+y
print('The Sum :',z)

#NOTE :- Input takes value string.

x = int(input('Enter x value :'))
print(x)
print(type(x))

Ex:- 
x = float(input('Enter x value :'))
print(x)
print(type(x))

# Note :- Add 2 strings.
x = input('Enter 1st String :')
y = input('Enter 2nd String :')

z = x + " " +y
print('The New String :', z)

# NOTE :- Expression.
# eval() # method

while(True):

    x = eval(input('Enter an expr :'))
    print(x)



