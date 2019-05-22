# your code goes here
s=input()
l=list(s)
j=len(l)-1
c=0
for i in s:
	if i==l[j] and j>=0:
		c=c+1
		j=j-1
	else:
		break
if c==len(l):
	print("yes")
else:
	print("no")
 #link list
