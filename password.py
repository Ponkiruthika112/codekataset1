a,b=map(str,input().split())
if len(a)>len(b):
    k=len(a)-len(b)
    for i in range(1,k+1):
        b=b+str(i)
else:
    k=len(b)-len(a)
    for i in range(1,k+1):
        a=a+str(i)
s=""
for i in range(0,len(a)):
        s=s+a[i]+b[i]
print(s)
#password
