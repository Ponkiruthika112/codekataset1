def call(a,b,p):
        s=""
        for i in range(p,len(a)):
                if a[i] in b and a[i] not in s:
                        if len(s)==0:
                                s=s+a[i]
                        elif b.index(s[-1])<b.index(a[i]):
                                s=s+a[i]
        return [len(s),s]
a=input()
b=input()
g=[]
for i in range(0,len(a)):
        g.append(call(a,b,i))
g.sort(reverse=True)
print(g[0][1])

#g
