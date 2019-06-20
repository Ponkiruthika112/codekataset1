n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,len(l)):
    if l[i]>l[i-1]:
        c=c+sum(l[0:i])
print(c)
#STAIRS
