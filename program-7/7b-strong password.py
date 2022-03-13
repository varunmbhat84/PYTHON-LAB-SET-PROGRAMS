import re
x = input ("Enter the password:")
y = True
while y:
    if (len (x) < 6 or len (x) > 16):
        print("The password is greater then 16 or lesser then 6") 
        print(" password invalid ")
        break
    elif not re.search ('[a-z]',x): 
        print ("The password dosen't contain lower case letter ")
        print ("password invalid")
        break
    elif not re.search ('[A-Z]', x): 
        print ("The password doesn't contain upper case letter")
        print ("password invalid")
        break
    elif not re.search ('[0-9]', x): 
        print ("The password doesn't contain numbers") 
        print ("password invalid") 
        break
    elif not re.search ('[$-_@%&^*#!]' , x): 
        print ("The password doesn't contain Special symbols")
        print("password invalid")
        break
    elif re.search ('\s',x):
        print ("The password contain Space")
        print("password invalid")
        break
    else:
        print("The password is valid")
        break
