n=int(input())
l=list(map(str,input().split()))
s="".join(l)
q=""
if n%2==0:
    k=((n)//2)-1
else:
    k=((n-1)//2)-1
p=list(s[0:k+1])
r=list(s[k+1:])
p.sort()
r.sort(reverse=True)
g=p+r
for i in g:
    q=q+i+" "
print(q.strip())
#rfghj
