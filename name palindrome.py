name="sas"
i=1
sum=""
while i<=len(name):
    sum+=name[-i]
    i+=1
if sum==name:
    print(sum,"paindrome")
else:
    print("not palimdrome",sum)