l=[1]
c=len(l)-1
for i in range(1):
    k=[]
    k=l[c:]+l[:c]
   
    
   
    if c==0:
        print('yes')
        c=len(l)
        k=[]
        k=l
    
    c-=1
    print(k)
print(k)
