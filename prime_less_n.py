def prime(n):
    l=[]
    for k in range(2,n):
        if k==2:
            l.append(2)
        else:
            for i in range(2,k):
                if k%i==0:
                    break
            if i==k-1:
                l.append(k)
    return l
n=int(input())
l=prime(n)
if len(l)==0:
    print(0)
else:
    print(*l)
#prime
