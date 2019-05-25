n,k=map(int,input().split())
l=list(map(int,input().split()))
s="empty"
for i in range(l.count(k)):
    l.remove(k)
if len(l)==0:
    print(s)
else:
    print(*l)
#g
