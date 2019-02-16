n,l,r=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
for i in p:
    if i>=l and i<=r:
        print(i)
        break
#pi
