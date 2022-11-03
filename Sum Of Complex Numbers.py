#Declaring two lists to store the real and imaginary parts of the complex number
rlist=[]
ilist=[]

#Taking input from the user
c1=input("Enter complex number - 1: ")
c2=input("Enter complex number - 2: ")

#Splitting the real part of the complex number 
if c1.startswith("-"):
  if "+" in c1:
    r1=c1.split("+")
    r1=r1[0]
    r1=int(r1)
  else:
    r1=c1.split("-")
    r1=r1[1]
    r1=int(r1)
    r1=-(r1)
else:
  if "+" in c1:
    r1=c1.split("+")
    r1=r1[0]
    r1=int(r1)
  else:
    r1=c1.split("-")
    r1=r1[0]
    r1=int(r1)

if c2.startswith("-"):
  if "+" in c2:
    r2=c2.split("+")
    r2=r2[0]
    r2=int(r2)
  else:
    r2=c2.split("-")
    r2=r2[1]
    r2=int(r2)
    r2=-(r2)
else:
  if "+" in c2:
    r2=c2.split("+")
    r2=r2[0]
    r2=int(r2)
  else:
    r2=c2.split("-")
    r2=r2[0]
    r2=int(r2)

#print(r1,r2)
rlist.append(r1)
rlist.append(r2)
r=sum(rlist)
#print(r)

#Splitting the complex part of the complex number
if "+" in c1:
  i1=c1.split("+")[1]
  i1=i1.split("i")[0]
  i1=int(i1)
else:
  i1=c1.split("-")[1]
  i1=i1.split("i")[0]
  i1=int(i1)
  i1=-i1

if "+" in c2:
  i2=c2.split("+")[1]
  i2=i2.split("i")[0]
  i2=int(i2)
else:
  i2=c2.split("-")[1]
  i2=i2.split("i")[0]
  i2=int(i2)
  i2=-i2


#print(i1,i2)
ilist.append(i1)
ilist.append(int(i2))
i=sum(ilist)
#print(i)

#Printing the result.
print("Sum of two complex numbers is",r,"+",i,"i")