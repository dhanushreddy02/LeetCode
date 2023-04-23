s='leetcode'
j=list(s)
k=[]
for i in j:
    if i not in k:
        k.append(i)
print(j)
print(k)
op=0
for i in k:
    if j.count(i)==1:
        print(i)
        op=j.index(i)
        break
print(op)
