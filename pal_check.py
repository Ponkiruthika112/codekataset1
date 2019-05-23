s=input()
c=0
for i in range(0,len(s)):
    k=s[0:i]+s[i+1::]
    if k==k[::-1]:
        c=c+1
        break
if c!=0:
    print("YES")
else:
    print("NO")
#pal
