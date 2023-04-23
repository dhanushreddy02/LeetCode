s="  helo world"
k=''
l=[]
for i in s:
    print(i)
    if i!=" ":
        k+=i
    else:
        l.append(k)
        k=''
print(l)
