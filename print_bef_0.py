n=int(input())
l=list(map(int,input().split()))
s=""
for i in range(0,len(l)):
    s=s+str(l[i])
k=""
i=0
p=-1
while i<len(s):
    if s[i]=="0" and s[i-1]=="0":
        i=i+1
    elif s[i]=="0":
        k=k+s[p+1:i]
        p=i
        i=i+1
    else:
        i=i+1
print(k)
        
#g,
