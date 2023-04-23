j=bin(5)
l=[]
for i in range(2,len(j)):
    l.append(j[i])
k=[]
print(l)
for i in l:
    if i=='1':
        k.append('0')
    else:
        k.append('1')
print(k)
op=0
c=0
for i in k[::-1]:
    op+=(2**c)*int(i)
    c+=1
print(op)
    
