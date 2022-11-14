n=int(input("Enter the Number: "))
count=0
for i in range(1,n+1):
    if (n%(i+1)==0):
        count=count+1
    i=i+1
if count>2:
    print(f"{n} is Composite")
else:
    print(f"{n} is not Composite, infact it is a Prime Number")