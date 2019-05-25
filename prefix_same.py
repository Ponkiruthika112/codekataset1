n=int(input())
l=list(map(str,input().split()))
s=input()
c=0
for i in l:
    if i[0:len(s)]==s:
        c=c+1
print(c)
#str
