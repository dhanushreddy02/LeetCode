n=int(input("enter:"))
l=[]
for i in range(1,n):
    c=0
    for j in range(2,n):
        if i%j==0:
            c=c+1
    if c==1:
        l.append(i)
print(len(l))
    
