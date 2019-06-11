def fun(n):
        a=[]
        k=bin(2**n-1)[2::]
        l=len(k)
        for i in range(0,2**n):
                s=bin(i)[2::]
                if len(s)<l:
                        a.append((l-len(s))*"0"+s)
                else:
                        a.append(s)
        for i in range(0,len(a)):
                a[i]=a[i].replace("0","3")
                a[i]=a[i].replace("1","4")
        return a
n=int(input())
l=[]
for i in range(1,n+1):
        l=l+fun(i)
        if len(l)>=n:
                break
print(l[n-1])
#d
	
