a= "good night sleep tight"
print("The string is",a)
d = dict()
for ch in a:
    d[ch] = d.get(ch,0)+1
print("Letters and frequency are:",d) 