n=int(input())
t=3
c=3
def check(n,p,t,j):
	
	for i in range(p+1,t+1):
		if i==n:
			k=j
			break
		j=j-1
	return k
if n<=3:
	j=3
	p=0
	t=3
	print(check(n,p,t,j))
	
else:
	while t<n:
		c=2*c
		p=t
		t=t+c
	j=c
	print(check(n,p,t,j))
  #jm
#zxc
