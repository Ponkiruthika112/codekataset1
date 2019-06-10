s=input()
c=0
if s.count("@")==1 and s.count(".")==1:
        c=c+1
for i in range(0,len(s)):
        if s[i]=="@":
                k=i
        if s[i]==".":
                p=i-k-1
if k>=3 and p<=5:
        c=c+1
if s[len(s)-4::]==".com":
        c=c+1
if c==3:
        print("YES")
else:
        print("NO")
#email
