n=int(input())
l=list(str(n))
s=0
k=[]
for i in range(0,len(l)):
	s=s+int(l[i])
	k.append(s)
print(sum(k))
#sum
