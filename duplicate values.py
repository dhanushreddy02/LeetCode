l=[0,0,0,0,1,1,1,2,2,3,3]
k=[]
for i in l:
    if i!=0:
        k.append(i)
print(k)
print(l)
l1=list(set(l))
print(l1)
j=[]
for i in l1:
    j.append(i)
k=len(l)-len(l1)
for i in range(k):
    j.append("_")
print(tuple(j))
