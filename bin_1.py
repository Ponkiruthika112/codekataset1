n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    s.append((bin(i)[2:]).count("1"))
k=[]
for i in range(0,n):
    k.append([l[i],s[i]])
k.sort(key=lambda x:x[1],reverse=True)
for i in range(0,len(k)):
    print(k[i][0])
#bin
