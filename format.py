n=int(input())
l=[]
for i in range(0,n):
    l.append(list(map(int,input().split())))
s=0
for i in l:
    s=s+sum(i)
print(format(s/(n*n),".6f"))
#format
