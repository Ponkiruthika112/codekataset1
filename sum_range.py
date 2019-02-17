n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,k):
    a,b=map(int,input().split())
    s=0
    for i in range(a-1,b):
        s=s+l[i]
    print(s)
#index
