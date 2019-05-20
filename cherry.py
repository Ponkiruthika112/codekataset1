# your code goes here
def cost(p):
	c=0
	if p=="R":
		c=c+5
	else:
		c=c+3
	return c
def call(s):
	if len(s)>2:
		i=0
		while i<len(s)-2:
			if s[i]==s[i+1]!=s[i+2]:
				c=cost(s[i])
			else:
				c=0
			return c
			i=i+2
	elif len(s)==2 and s[0]==s[1]:
		c=cost(s[0])
		return c
	else:
		c=0
		return c
		
	
n,m=map(int,input().split())
l=[]
s=[]
for i in range(0,n):
	l.append(input())
for i in range(0,len(l)):
	s.append(call(l[i]))
print(sum(s))
#cherry
