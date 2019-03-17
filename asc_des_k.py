n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
b=[]
p=""
for i in range(0,k):
    a.append(l[i])
for i in range(k,len(l)):
    b.append(l[i])
a.sort()
b.sort(reverse=True)
c=a+b
for i in range(0,len(c)):
    p=p+str(c[i])+" "
print(p.strip())
    
#ascendig and descending
