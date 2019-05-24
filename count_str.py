s=input()
c=1
l=[]
d=s[0]
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        c=c+1
        d=s[i]
    else:
        l.append([c,d])
        c=1
        d=s[i]
l.append([c,d])
r=""
for i in l:
    if i[0]==1:
        r=r+i[1]
    else:
        r=r+str(i[0])+"*"+i[1]
print(r)
#count
