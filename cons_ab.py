s=input()
c=[]
if s.find("ab")!=-1:
	for i in range(0,len(s)-1):
		if s[i]=="a" and s[i+1]=="b":
			c.append(i)
	
	l=[]
	t=1
	for i in range(0,len(c)-1):
		if c[i+1]-c[i]==2:
			t=t+1
		else:
			l.append(t)
			t=1
	l.append(t)
	if s[len(s)-1]=="a" and s[len(s)-2]=="b":
		print((max(l)*2)+1)
	else:
		print(max(l)*2)
else:
	print(0)
#cons
