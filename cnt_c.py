def count(i,p):
    c=0
    k=str(i)
    if k.count(str(p))!=0:
        c=c+1
    return c
    
a,b,c=map(int,input().split())
j=0
for i in range(a,b):
    j=j+count(i,c)
print(j)
#hj
