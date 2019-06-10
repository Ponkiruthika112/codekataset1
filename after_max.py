n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,len(l)-1):
        s.append(max(l[i+1::]))
s.append(0)
print(*s)
        
#gf
