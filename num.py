n=int(input())
l=list(map(int,input().split()))
k=list(dict.fromkeys(l))
if l==k:
    print("unique")
else:
    for i in k:
        if l.count(i)>1:
            print(i)
            break
#fghjk
