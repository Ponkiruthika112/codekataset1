n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)-1):
    c=c+l[i]+l[i+1]
print(c)
#h
