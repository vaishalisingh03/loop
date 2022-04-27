# i=1
# # k=1
# while i<5:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#         # k+=1
#     print()
#     i+=1
# a=[1,2,[4,6],8]
# i=0
# s=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             s.append(a[i][j])
#             j+=1
#     else:
#         s.append(a[i])
#     i+=1
# print(s)
a=[1,2,4,5,6,90,56,8,9,5,4,2,1,4,6]
i=0
k=[]
l=[]
count=0
while i<len(a):
    if count==3:
        k.append(l)
        l=[]
        count=1
    else:
        count+=1
    l.append(a[i])
    i+=1
k.append(l)
print(k)



