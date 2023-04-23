n=28
l=[]
for i in range(1,(n//2)+1):
    if n%i==0:
        l.append(i)
print(l)
print(sum(l))
