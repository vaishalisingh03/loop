i=int(input("enter number"))
a=int(input("enter number"))
while i<=a:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print("prime number",i)
    i+=1
