def sum(l):
    s=0
    for i in range(1,len(l)):
        s=s+int(l[i])
    return s
a=input()
b=input()
x=a.split("#")
y=b.split("#")
if sum(x)>sum(y):
    print(x[0])
else:
    print(y[0])
#max
