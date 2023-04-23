l=[10,4,8,3]
ri=[]
le=[]
res=[]
for i in range(len(l)):
    k=l[:i]
    le.append(sum(k))
print(le)
j=l[::-1]
for i in range(len(l)):
    s=j[:i]
    ri.append(sum(s))
ri=ri[::-1]
for i in range(len(ri)):
    res.append(ri[i]-le[i])
op=[]
for i in res:
    if i<0:
        i=str(i)
        op.append(int(i[1:]))
    else:
        op.append(i)
print(op)
