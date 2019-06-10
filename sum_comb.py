from itertools import combinations
n,k,r=map(int,input().split())
s=list(map(int,input().split()))

p=list(combinations(s,k))
c=list(set(p))
t=[]
for i in range(0,len(c)):
        t.append(sum(list(c[i])))
if t.count(r)==0:
        print("NO")
else:
        print("YES")
#comb
