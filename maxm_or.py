n=int(input())
l=list(map(int,input().split()))
c=l[0]
for i in range(1,len(l)):
    c=c|l[i]
print(c)
#maxma
