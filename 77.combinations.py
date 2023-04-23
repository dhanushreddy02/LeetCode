n=10
k=7
j=''
for i in range(1,n+1):
    j+=str(i)
from itertools import combinations
k=list(combinations(j,k))
l=[]
for i in k:
    i=(list(i))
    z=[]
    for el in i:
        z.append(int(el))
    l.append(z)
print(l)
