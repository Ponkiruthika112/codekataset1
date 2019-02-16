n,k=map(int,input().split())
l=[]
for i in range(0,n):
    l.append(list(map(int,input().split())))
for i in range(0,len(l)):
    if l[i][1]==k:
        print("YES")
    else:
        print("NO")
    
#reach
