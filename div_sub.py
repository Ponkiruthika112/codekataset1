a,b=map(int,input().split())
c=0
if a<b:
    c=0
else:
    while a>0:
        a=a-b
        c=c+1
print(c)
#div
