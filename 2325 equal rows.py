l=[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
row=[]
for i in range(len(l)):
    k=[]
    for j in range(len(l)):
        k.append(l[j][i])
    row.append(k)
c=0
print(row)
k=[]
for i in l:
    if i not in k:
        k.append(i)
print(l)
print

for i in k:
    c+=row.count(i)
print(c)
                
        
