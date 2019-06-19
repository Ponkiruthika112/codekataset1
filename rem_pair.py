n=input()
for i in range(len(n)-1,0,-1):
    if n[i]==n[i-1]:
        s=n[i]
        k=i
        n=n.replace(n[i],"*")
        break
n=n.replace("**",s)
n=n.replace("*",s)
print(n)
#pj
