# WAP to print Reverse the string by using Reversed Function and take the input from the user.
s=input("Enter some string to Reverse :")
r=reversed(s)
print(type(r))
for ch in r:
    print(ch)


# NOTE :- IF you don't want string in the character form then you use the full string without any space.

print('**********************************')

s=input('Enter the some string to Reversed :')
r=reversed(s) # in-built function.
output=''.join(r)
print(output)

