s=input()
a=0
b=0
l=[]
k=""
for i in range(0,len(s)):
    if s[i]==" ":
        b=i
        l.append(s[a:b])
        a=i+1
l.append(s[a::])
if len(l)>2:
    for i in range(0,len(l)):
        if l[i]=="and":
            l[i-1],l[i+1]=l[i+1],l[i-1]
for i in l:
    k=k+i+" "
print(k.strip())
#interchange the words
