n=input()
l=list(map(int,input().split()))
p=1
k=[]
for i in l:
	p=p*i
for i in range(0,len(l)):
	k.append(p//l[i])
print(*k)
#product
