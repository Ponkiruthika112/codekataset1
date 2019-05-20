n,m=map(int,input().split())
l=[]
k=[]
for i in range(0,n):
	l.append(list(map(int,input().split())))
for i in range(0,len(l)):
	for j in range(0,len(l)):
		if l[i][j]==0:
			k.append([i,j])
for g in range(0,len(k)):
	a=k[g][0]
	b=k[g][1]

	for i in range(0,len(l)):
		l[a][i]=0
		
	for j in range(0,len(l)):
		l[j][b]=0
for i in range(0,len(l)):
	print(*l[i])
#zeros
