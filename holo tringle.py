num=int(input("enter the number"))
i=0
while i<=num:
    j=0
    while j<i:
        if j==0 or j==i-1:
            print("*",end=" ")
        else:
            if i!=num:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        j=j+1
    print()
    i=i+1
