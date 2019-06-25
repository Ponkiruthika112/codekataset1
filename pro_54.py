n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(0,len(a)):
        l.append(b[i]//a[i])
p=min(l)
for i in range(0,k):
        g=l.index(p)
        l[g]=(b[g]+1)//a[g]
        p=min(l)
print(min(l))
#d
