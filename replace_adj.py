n=int(input())
l=list(map(int,input().split()))
i=0
if n%2==0:
    k=len(l)-1
else:
    k=len(l)-2
while i<k:
    l[i],l[i+1]=l[i+1],l[i]
    i=i+1
s=""
for i in l:
    s=s+str(i)+" "
print(s.strip())
#replace
