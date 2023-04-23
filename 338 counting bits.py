n=5
l=[]
for i in range(n+1):
    k=str(bin(i))
    print(k)
    l.append(k.count('1'))
print(l)
