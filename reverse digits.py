i=int(input("enter digits>:"))
rev=0
while i>0:
    rev=rev*10+i%10
    i//=10
print(rev)