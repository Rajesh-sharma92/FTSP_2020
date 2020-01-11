# WAP to print the string in the reverse order by using While Loop.

s=input('Enter some string to print in reverse order :')
output=''
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
    print(output)
    
