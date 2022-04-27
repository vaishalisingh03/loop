i=1
list=[]
while i<=100:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1   
        j+=1
    if count==2:
        list.append(i)
    i+=1
print(list)










