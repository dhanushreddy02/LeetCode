class mystack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        
        return self.stack.pop(0)
    def top(self):
        return self.stack[-1]
    def ismt(self):
        if len(self.stack)==0:
            return True
        else:
            return False
z=mystack()
z.push(10)
z.push(20)

print(z.pop())
print(z.top())
print(z.ismt())
