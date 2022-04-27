i=int(input("enter digits"))
prod=1
while i>0:
    prod*=i%10
    i//=10
print(prod)