a = input("Enter a string:")
print("The input string is:",a)
b = a[::-1]
print("The reverse of the given string is:",b)
c = b.replace(' ','')
print("The reverse string after removing space is:",c)
d = c[0::2]
print("Print odd places:",d)