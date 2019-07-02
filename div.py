a=input()
b=input()
c=""
for i in a:
    if i not in c:
        c=c+i
k=b.count(c)
if k==1:
    print(1)
else:
    print(k//len(c))
#s
