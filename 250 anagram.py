j='ac'
k='abbc'
j=list(j)
k=list(k)
j1=len(j)
k1=len(k)
while j1!=k1:
    if j1>k1:
        k.append('0')
        k1+=1
    else:
        j.append('0')
        j1+=1
print(k)
print(j)
