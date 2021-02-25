

inp=int(input("Enter The number for calcultion:"))
a=int(input("Enter The number for calcultion:"))
op=input("Enter the operator +\n-\n*\n/\n**\n%:")
z=str(inp)+str(op)+str(a)
print(z)

l=str("45*3")
m=str("56+9")
n=str("56/6")

if z==l:
    print("555")
elif z==m:
    print("77")
elif z==n:
    print("4")
elif (op=="*"):
    i=int(inp)*int(a)
    print(i)
elif (op=="+"):
    i=int(inp)+int(a)
    print(i)
elif (op=="-"):
    i=int(inp)-int(a)
    print(i)
elif (op=="%"):
    i=int(inp)%int(a)
    print(i)
elif (op=="**"):
    i=int(inp)**int(a)
    print(i)
else:
    print('Please select correct input')
