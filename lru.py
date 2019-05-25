n,k=map(int,input().split())
l=list(map(int,input().split()))
p=len(l)-k
r=""
for i in range(p,len(l)):
    r=r+str(l[i])+" "
print(r.strip())
#lru
