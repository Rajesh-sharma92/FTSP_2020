# WAP to print the Contents of the each word and take the input from User.

s=input('Enter some string and print each words contents in the reverse order \n')
l=s.split()
l1=[]
for word in l:
    l1.append(word[: : -1])
    print(l1)

    output=' '.join(l1)
    print(output)
    
    
    
