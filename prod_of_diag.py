n=int(input())
l=[]
s=0
k=0
for i in range(0,n):
    l.append(list(map(int,input().split())))
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            s=s+l[i][j]
        if i+j==n-1:
            k=k+l[i][j]
print(s*k)

#product of diagnal
