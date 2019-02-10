s,k=map(str,input().split())
j=int(k)
g=j%len(s)
l=""
l=l+s[-g:len(s)]
l=l+s[0:len(s)-g]
print(l)
#rotation
