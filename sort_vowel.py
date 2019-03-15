def count(s):
    k=0
    for i in s:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            k=k+1
    return k
n=int(input())
l=[]
for i in range(0,n):
    s=input()
    l.append([s,count(s)])
l.sort(key=lambda x:x[1],reverse=True)
for i in range(0,len(l)):
    print(l[i][0])
#based on vowel 
