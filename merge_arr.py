n=int(input())
k=[]
for i in range(0,n):
	l=list(map(int,input().split()))
	k=k+l
k.sort()
print(*k)
#merge
