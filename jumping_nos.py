def con(n):
    s=list(str(n))
    c=0
    for i in range(0,len(s)-1):
        if abs(int(s[i])-int(s[i+1]))==1:
            c=c+1
    if c==len(s)-1:
        return 1
    else:
        return 0
        
               
n=int(input())
c=10
k=(n//10)-2 
if n<=10:
    print(n+1)
else:
    c=c+2*k
    for i in range(((k+1)*10)+1,n):
        if con(i)==1:
            c=c+1
    print(c)


#cv
