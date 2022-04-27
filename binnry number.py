num=int(input("enter binnry number"))
sum=0
i=0
while num>0:
    rev=num%10
    num=num//10
    sum+=rev*(2**i)
    i+=1
print("decimal",sum)


    