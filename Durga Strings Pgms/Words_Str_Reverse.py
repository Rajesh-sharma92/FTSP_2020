# WAP to print the words from string in reverse order and take the input from string.

# s='Learning Python is very easy'

s=input('Enter some string to reverse :')
l=s.split()
print(l)
l1=l[: :-1] # The Output will be in the form of List.
print(l1)
output=' '.join(l1)
s.count(l1)
print(output)



