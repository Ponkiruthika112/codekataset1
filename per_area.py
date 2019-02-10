p,a=map(int,input().split())
l=[]
c=0
for i in range(1,a):
    if a%i==0:
        l.append(i)
print(l)
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if l[i]*l[j]==a and 2*(l[i]+l[j])==p:
            c=c+1
            
if c!=0:
    print("yes")
else:
    print("no")
#perimeter and area of rectangle
