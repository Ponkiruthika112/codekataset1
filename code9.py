#this is to sum
n,k=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in range(0,k):
  s=s+l[i]
print(s)
