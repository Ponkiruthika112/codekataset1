n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
j=len(l)-1
for i in range(0,len(l)):
    if l[i]==k[j]:
        c=c+1
    j=j-1
        
if c==len(l):
    print("yes")
else:
    print("no")
#mirror
