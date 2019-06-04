def fact(n):
	c=1
	for i in range(1,n+1):
		c=c*i
	return c
def comb(n,r):
	f=fact(n)//(fact(n-r)*fact(r))
	return f
	
n=int(input())
c=1
k=n//2
if 2*k==n:
	c=c+1
	for i in range(1,k):
		if i==k-1:
			c=c+comb(k+i,(n-2*(k-i)))
		else:
			c=c+comb(k+i,k-i+(n-2*(k-i)))
elif n==1:
	c=n
	
else:
	c=c+comb(k+1,k)
	for i in range(1,k):
		if i==k-1:
			c=c+comb(k+(2*i),(n-2*(k-i)))
		else:
			c=c+comb(k+(2*i),k-i+(n-2*(k-i)))
print(c)

#c
