n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in range(0,len(a)-2):
    if a[i]<a[i+1] and a[i+1]>a[i+2]:
        c=c+1
    elif a[i]>a[i+1] and a[i+1]<a[i+2]:
        k=k+1
if c+k==len(a)-2:
    print("yes")
else:
    print("no")
#alter inc dec
