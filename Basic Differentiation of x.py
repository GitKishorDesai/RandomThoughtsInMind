str="Prefix (x) ^power"
print(str)

pref=input("Enter the prefix of x: ")
try:
    pref=float(pref)
    print(pref,"(x) ^power")
except:
    print("Enter numerical value of prefix of x, don't use fractions")


power=input("Enter the power of x: ")
try:
    power=float(power)
    print(pref,"(x) ^",power)
except:
    print("Enter numerical value of power of x, don't use fractions")


print("Is the above expression correct? Mention it below...")
uinp=input()

if uinp=="yes" or uinp=="YES" or uinp=="Yes":
    print(pref*power,"(x) ^",(power-1))
else:
    print("To re-write, please start the program again")