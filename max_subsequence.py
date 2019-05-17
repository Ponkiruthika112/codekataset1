n=int(input())
l=list(map(int,input().split()))
c=1
p=[]
for i in range(1,len(l)):
	if l[i]-l[i-1]==1:
		c=c+1
	else:
		p.append(c)
		c=1
p.append(c)
print(max(p))
#subsequence
