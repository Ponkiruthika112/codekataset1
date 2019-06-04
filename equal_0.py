# your code goes here
n=int(input())
l=list(map(int,input().split()))
k=10000
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		c=abs(l[i]+l[j])
		if c<k:
			k=abs(l[i]+l[j])
			p=l[i]
			q=l[j]
print(p,q)
#p
