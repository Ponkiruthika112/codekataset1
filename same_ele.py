a,b=map(int,input().split())
l=[]
c=1
k=[]
for i in range(0,a):
        l.append(list(map(int,input().split())))
for i in range(0,len(l[0])):
        for j in range(1,len(l)):
                if l[j].count(l[0][i])>0:
                        c=c+1
        if c==len(l):
                k.append(l[0][i])

        c=1
k.sort()
print(*k)
#same
