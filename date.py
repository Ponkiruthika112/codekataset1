s=input()
a=0
b=0
c=0
l=[]
p=[1,3,5,7,8,10,12]
q=[4,6,9,11]
for i in range(0,len(s)):
    if s[i]=="/":
        b=i
        l.append(s[a:b])
        a=i+1
l.append(s[a::])
if len(l[0])==2 and len(l[1])==2:
    if p.count(int(l[1]))==1 and int(l[0])>=1 and int(l[0])<=31:
        c=c+1
    elif q.count(int(l[1]))==1 and int(l[0])>=1 and int(l[0])<=30:
        c=c+1
    elif int(l[1])==2 and int(l[0])>=1 and int(l[0])<=29:
        c=c+1
if len(l[2])==4:
    c=c+1
    
if c==2:
    print("yes")
else:
    print("no")
#date
