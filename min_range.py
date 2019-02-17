n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,k):
    a,b=map(int,input().split())
    s=[]
    for i in range(a-1,b):
        s.append(l[i])
    print(min(s))
#min range
