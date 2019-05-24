def fact(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return(l)
n,m=map(int,input().split())
a=fact(n)
b=fact(m)
p=list(set(a+b))
if len(p)==len(a)+len(b)-1:
    print("yes")
else:
    print("no")
                                                                                   
#coprime
