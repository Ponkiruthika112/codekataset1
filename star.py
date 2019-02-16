n=int(input())
l=list(map(int,input().split()))
m=max(l)
k=l.index(m)
s=""
for i in range(k,len(l)):
    c=0
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            c=c+1
    if c==len(l)-i-1:
        s=s+str(l[i])+" "
print(s.strip())
print(m)

#star
