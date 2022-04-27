i=int(input("enter digits"))
p=int(input("enter number"))
org=i
sum=0
while i>0:
    sum=sum+(i%10)**p
    i//=10
if org==sum:
    print("this num is armstrong",sum)
else:
    print("this num is not armstrong",sum)

