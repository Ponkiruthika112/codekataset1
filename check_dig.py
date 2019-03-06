n,k=map(str,input().split())
c=0
for i in range(0,int(k)+1):
    if n.count(str(i))>=1:
        c=c+1
if c==int(k)+1:
    print("yes")
else:
    print("no")
#heck digits 
