n=int(input())
s=0
l=list(str(n))
for i in l:
    s=s+int(i)
k=str(s)
if k==k[::-1]:
    print("YES")
else:
    print("NO")
#sum
