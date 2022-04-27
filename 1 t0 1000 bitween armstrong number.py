i=1
list=[]
while i<=1000:
    j=i
    sum=0
    org=j
    while j>0:
        sum=sum+(j%10)**3
        j//=10
    if sum==org:
        list.append(sum)
    i+=1
print(list)