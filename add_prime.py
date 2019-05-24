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
c=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==n:
            print(l[i],l[j])
            c=1
    if c==1:
        break
#add
