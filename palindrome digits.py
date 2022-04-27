num=int(input("ener digits"))
i=num
rev=0
while num>0:
    rev=rev*10+num%10
    num//=10
if i==rev:
    print("pailndrome",rev)
else:
    print("not pailmdrom",rev)
