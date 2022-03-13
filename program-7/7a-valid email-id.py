import re
a = re.compile(r'[a-zA-Z0-9]+[\@][a-z]+[\.][a-z]\.?[a-z]*')
b = input("Enter a valid email id:")
c = a.findall(b)
if a.findall(b):
    print(c)
else:
    print("Invalied email id")