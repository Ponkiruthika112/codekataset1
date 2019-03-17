s,k=map(str,input().split())
n=int(k)
c=n-1
k=""
i=0
while i<len(s):
    if i!=c:
        k=k+s[i]
    else:
        k=k+s[i].upper()
        c=c+n
    i=i+1
print(k)
                                   
        
#string k th letter will be converted to upper case
