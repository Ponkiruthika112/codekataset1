n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)-1,0,-1):
        print(l[i],end="->")
print(l[0])
        
#reverse
