s=input()
c=0
l=[]
d=s[0]
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c=c+1
        d=s[i]
    else:
        l.append([c,d])
        c=1
l.append([c,d])
l.sort(reverse=True)
print(l[0][1],l[0][0])
        
#maxx conse 
