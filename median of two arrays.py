k=[1,3]
l=[2,4]
for i in l:
    k.append(i)
k.sort()
y=len(k)
if y%2!=0:
    print(float(k[((y+1)//2)-1]))
else:
    op=k[(y//2)-1]
    op1=k[(y//2)]
    print(double((op+op1)/2))
    
