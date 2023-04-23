left=1
right=22
op=[]
co=0
for i in range(left,right+1):
    co=0
    j=list(str(i))
    j=list(set(j))
    if '0' in j:
        j.remove('0')
        co=1
    
    
    for k in j:
        k=int(k)
        if i%k!=0:
            co=1
    print(i,co,j)
    if co!=1:
        op.append(i)
print(op)
