def factors(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    return l

a,b=map(str,input().split())
k=factors(len(a))
h=factors(len(b))
k.remove(k[0])
h.remove(h[0])
l=k+h
for i in range(0,len(l)):
    if l.count(l[i])>1:
        print("no")
        break
if i==len(l)-1:
    print("yes")
#coprime
