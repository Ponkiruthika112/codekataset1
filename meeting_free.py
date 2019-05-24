n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
for i in range(0,len(l)):
    p.append(k-l[i])
c=0
for i in p:
    if i<=0:
        c=c+1
print(c)
#meeting
