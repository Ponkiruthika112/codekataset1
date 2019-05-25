n,k=map(int,input().split())
l=list(map(int,input().split()))
i=k%n
g=l[i::]+l[0:i]
print(*g)
#rotate
