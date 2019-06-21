n=int(input())
l=list(map(int,input().split()))
p=[]
c=1
for i in range(0,len(l)):
    if l[i] not in p:
        p.append(l[i])
for i in range(0,len(p)-1):
    if p[i]<p[i+1]:
        c=c+1
print(c)
#lon
