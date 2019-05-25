n=int(input())
s=""
l=list(map(int,input().split()))
for i in range(0,len(l)-1):
    if l[i]>l[i+1]:
        s=s+str(l[i+1])+" "
    else:
        s=s+"-1"+" "
s=s+"-1"+" "
print(s.strip())
#small
