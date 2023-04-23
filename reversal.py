x=input()
y=str(x)
l=[]
ca=0
op=''
for i in y:
    if i in "1234567890":
        l.append(int(i))
    else:

        l.append(i)


if l[0]=="-":
    l.remove("-")
    
    ca+=1
l=l[::-1]
if l[0]==0:
    if len(l)>1:
        l.remove(0)


for i in l:
    op+=str(i)
op=int(op)
if ca==1:
    if op<2147483647:
        return(int("-"+str(op)))
    else:
        return(0)
    
else:
    if op<2147483647:
        return(int(op))
    else:
        return(0)
        
        
