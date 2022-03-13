a = ";virat@gmail.com;abd@gmail.com;smith@gmail.com;kame@gmail.com;love_is_blind@gmail.com;"
print("The given mail_id are:",a)
b = a.find(';')
c = a.find(';',b+1)
print("The mail id are:")
while (b!=-1):
    print(a[b+1:c])
    b = c
    c = a.find(';',b+1)

