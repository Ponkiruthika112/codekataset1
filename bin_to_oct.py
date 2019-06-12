def con(r):
    c=0
    if r[0]=="1":
        c=c+4
    if r[1]=="1":
        c=c+2
    if r[2]=="1":
        c=c+1
    return c
n=int(input())
s=str(n)
p=""
k=len(s)%3
if k!=0:
    g=3-k
    p=p+str(con(g*"0"+s[0:k]))
i=k
while i<=len(s)-3:
    p=p+str(con(s[i:i+3]))
    i=i+3
print(p)
#bin to oct
    
        
    
