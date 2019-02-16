s=input()
l=[]
c=0
for i in range(0,len(s)-1):
    k=int(s[i])+int(s[i+1])
    if k%2!=0:
        c=c+1
    else:
        l.append(c)
        c=0
    l.append(c)
p=max(l)
if p==0:
    print(0)
else:
    print(p+1)
#oo
