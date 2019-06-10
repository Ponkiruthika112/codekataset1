n=int(input())
l=[1000,500,100,50,10,1]
s=[]
c=0
for i in range(0,len(l)):
        k=n//l[i]
        c=c+k
        n=n-(k*l[i])
print(c)
#coinscount_coins
