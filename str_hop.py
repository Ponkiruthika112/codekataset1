s,k=map(str,input().split())
n=int(k)
k=s[n-1::n]
t=""
for i in k:
    t=t+i+" "
print(t.strip())
#print string
