def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

def arr(l):
    a=l[0]
    b=l[1]
    g=gcd(a,b)
    for i in range(2,len(l)):
        g=gcd(g,l[i])
    return g
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,k):
    a,b=map(int,input().split())
    if a==b:
        print(l[a-1])
    else:
        print(arr(l[a-1:b]))
#bb
