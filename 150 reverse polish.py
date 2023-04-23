k=[]
op=0
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

for i in tokens:
    op=0
    if i not in '+-*/':
        if int(i)>=200 or int(i)<=200:
            k.append(i)
    
            
    elif i in '+*-/':
        print(k)
        if i=="+":
            
            
            op=int(k[-1])+int(k[-2])
            k.remove(k[-1])
            k.remove(k[-1])
            k.append(op)
        elif i=="-":
            
            op=int(k[-2])-int(k[-1])
            k.remove(k[-1])
            k.remove(k[-1])
            k.append(op)
        elif i=="*":
            
            op=int(k[-1])*int(k[-2])
            k.remove(k[-1])
            k.remove(k[-1])
            k.append(op)
        else:
            
            op=int(k[-2])/int(k[-1])
            k.remove(k[-1])
            k.remove(k[-1])
            k.append(op)
    
print(k)                  
                
                   
