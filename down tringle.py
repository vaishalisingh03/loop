i=7
while i>=0:
    s=1
    while s<=7-i:
        print("",end=" ")
        s+=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i-=2