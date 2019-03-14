n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
p=[]
for i in k:
    p.append(l.count(i))
print(k[p.index(min(p))])
#array
