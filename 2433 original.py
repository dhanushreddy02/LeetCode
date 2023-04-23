l=[5,2,0,3,1]
k=[]
for i in range(len(l)-1):
    k.append(l[i]^l[i+1])
print(k)
k.insert(0,l[0])
print(k)
