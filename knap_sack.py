# your code goes here
# your code goes here
n,u=map(int,input().split())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
p=[]
q=[]
c=0
for i in range(0,len(v)):
	p.append([w[i],v[i]])
for i in range(0,len(v)):
	for j in range(0,len(v)):
		s=0
		d=0
		for k in range(i,j+1):
			s=s+p[k][0]
			d=d+p[k][1]
			q.append([s,d])
q.sort(key=lambda x:x[1],reverse=True)
for i in q:
	if i[0]<=u:
		c=c+1
		z=i[1]
		break
if c==0:
	print(0)
else:
	print(z)
#knapsack
