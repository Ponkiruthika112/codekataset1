n=int(input())
l=list(map(int,input().split()))
k=l
while len(l)>1:
	l=l[1::2]
print(k.index(l[0]))
#even pos
