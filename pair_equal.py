# your code goes here
n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==m:
			c=c+1
			break
if c==0:
	print("NO")
else:
	print("YES")
#EQUAL TO M
