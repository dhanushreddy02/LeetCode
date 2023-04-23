n=00000010100101000001111010011100
j=str(n)
summ=c=0
for i in j:
    summ+=((2**c)*int(i))
    c+=1
print(summ)
