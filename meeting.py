n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(0,n):
	l.append([a[i],b[i]])
start=l[0][0]
stop=l[0][1]
c=1
for i in range(1,len(l)):
	if stop<=l[i][0]:
		start=l[i][0]
		stop=l[i][1]
		c=c+1
print(c)
#meeting
