l=[["W","E","L","C","O"],["M","E","T","O","G"],["U","V","I","C","O"],["R","P","O","R","A"],["T","I","O","N","S"]]
s=input()
c=0
for i in range(0,5):
    k=""
    for j in range(0,5):
        k=k+l[j][i]
        if k.find(s)!=-1:
            d=k
            n=i
            m=k.index(s)
            c=1
            break
if c==1:
    print(m,n)
    print(m+len(s)-1,n)
else:
    print(0)
#HH
