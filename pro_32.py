a,b=map(int,input().split())
if a>b:
    a,b=b,a
k=[]
for i in range(a):
    l=list(map(int,input().split()))
    l.sort()
    k.append(l)
for j in range(0,b):
    p=[]
    for i in range(0,a):
        p.append(k[i][j])
    p.sort()
    r=0
    for i in range(0,a):
        k[i][j]=p[r]
        r=r+1
for i in k:
    print(*i)
    

#h
