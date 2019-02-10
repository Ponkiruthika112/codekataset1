s,k=map(str,input().split())
j=int(k)
g=j%len(s)
l=""
if g!=0:
    l=l+s[-g:len(s)]
    l=l+s[0:len(s)-g]
else:
    l=s
print(l)
#string rotation
