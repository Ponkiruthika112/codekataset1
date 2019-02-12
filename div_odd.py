n=int(input())
c=0
for i in range(1,n):
	p=n//i
	if n%i==0 and p%2==1:
		print(i)
		c=c+1
		break
#odd
