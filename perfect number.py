num=int(input("enter number"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i+=1
if sum==num:
    print(sum,"is perfect num")
else:
    print(sum,"is not perfect num")