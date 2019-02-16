n=int(input())
l=list(map(str,input().split()))
s="".join(l)
print(s)
q=""
if n%2==0:
    k=(n-1)//2
else:
    k=(n-2)//2
p=list(s[0:k+1])
r=list(s[k+1:])
p.sort()
r.sort(reverse=True)
g=p+r
for i in g:
    q=q+i+" "
print(q.strip())
#hf'
