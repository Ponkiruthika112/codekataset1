# your code goes here
n,k=map(int,input().split())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
p=[]
q=[]
c=0
for i in range(0,len(v)):
	p.append([w[i],v[i]])
for i in range(0,len(v)):
	s=0
	d=0
	
	for j in range(0,len(v)):
		s=s+p[j][0]
		d=d+p[j][1]
		q.append([s,d])
q.sort(reverse=True)
for i in q:
	if i[0]<=k:
		c=c+1
		break
if c==0:
	print(0)
else:
	print(i[1])
#knapsack
