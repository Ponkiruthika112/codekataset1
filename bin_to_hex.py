def con(r):
    c=0
    if r[0]=="1":
        c=c+8
    if r[1]=="1":
        c=c+4
    if r[2]=="1":
        c=c+2
    if r[3]=="1":
        c=c+1
    return c
def call(m):
    if m==10:
        p="A"
    if m==11:
        p="B"
    if m==12:
        p="C"
    if m==13:
        p="D"
    if m==14:
        p="E"
    if m==15:
        p="F"
    return p

n=int(input())
s=str(n)
p=""
k=len(s)%4
if k!=0:
    g=4-k
    m=con(g*"0"+s[0:k])
    if m<10:
        p=p+str(con(g*"0"+s[0:k]))
    else:
        p=p+call(m)
            
i=k
while i<=len(s)-4:
    q=con(s[i:i+4])
    if q<10:
        p=p+str(con(s[i:i+4]))
    else:
        p=p+call(q)
    i=i+4
print(p)
#bn to hex
    
   
