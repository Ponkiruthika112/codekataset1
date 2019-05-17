n=int(input())
l=list(str(n))
s=0
for i in range(0,len(l)):
	s=s+(int(l[i]))**len(l)
	
print(s)
#power sum
