n=int(input())
y=list(map(int,input().split()))
c=0
for i in range(0,len(y)):
	for j in range(1,len(y)+1):
		k=y[i:j]
		s=y[0:i]+y[j::]
	
	if len(s)==0 or len(k)==0:
	    c=0
	else:
	    if (sum(k)//len(k))==(sum(s)//len(s)):
	        c=c+1
	    
if c==0:
	print("no")
else:
	print("yes")
 #average
