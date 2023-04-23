x="1213"
l=[]
ca=0
rev=""
for i in x:
    if i in "1234567890":
        l.append(i)
    else:
        ca=1
for i in l[::-1]:
    rev+=i
if ca!=1:
    if rev==x:
        print(True)
    else:
        print(False)
else:
    print(False)
    
