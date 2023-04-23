n=int(input())
j=""
for i in range(1,n+1):
    j+=str(i)
from itertools import permutations
l=list(permutations(j))
k=list(l[3-1])
op=''
for i in k:
    op+=i
print(op)

