l=[0,2,3,4,6,8,9]
k=[]
op=[]
for i in range(1,len(l)):
    if l[i]-l[i-1]==1:
        k.append(l[i])
    else:
        for i in k:
            op.append(i)
print(op)
