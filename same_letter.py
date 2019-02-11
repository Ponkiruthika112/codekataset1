a,b=map(str,input().split())
for i in a:
    a=a.replace(i,"*")
    b=b.replace(i,"*")
if b.count("*")>0:
    print("yes")
else:
    print("no")
#same one
