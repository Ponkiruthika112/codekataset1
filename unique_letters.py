# your code goes here
s=input()
l=list(s)
k=list(set(list(s)))
p=[]
for i in range(0,len(k)):
	p.append([l.index(k[i]),k[i]])
p.sort()
f=""
for i in range(0,len(k)):
	f=f+p[i][1]
print(f)
#UNIQUE
