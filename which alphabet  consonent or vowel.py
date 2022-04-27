a=input("enter albhabet")
i=0
while i<len(a):
    if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
        print("vovell",a[i])
    else:
        print("consonent",a[i])
    i=i+1
