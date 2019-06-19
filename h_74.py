a=input()
b=input()
l=[]
if a==b:
    l.append([1,a])
else:
    for i in range(0,len(a)):
        for j in range(len(a),-1,-1):
            if b.find(a[i:j+1])!=-1:
                l.append([len(a[i:j+1]),a[i:j+1]])
                break

l.sort(reverse=True)
print(l[0][1])
#dfv
