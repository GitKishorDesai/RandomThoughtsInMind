var1=1
sum=0
i=1
j=1
x=int(input("Enter x: "))
print(f"borga(x) is borga({x})")
while (i>0):
    var2=1
    for j in range(1,((2*i)+2)):
        var2=var2*j
    #print("-----------")
    var1=var1*x
    #print(var1)
    #print(var2)
    if ((var1)/(var2))>0.000001:
        sum=sum+(var1/var2)
        i=i+1
    else:
        break
print(f"borga({x})={(1+sum):.3f}")