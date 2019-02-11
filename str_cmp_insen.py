a,b=map(str,input().split())
c=0
if len(a)==len(b):
    for i in range(0,len(a)):
        if a[i]==b[i] or a[i]==b[i].upper() or a[i]==b[i].lower():
            c=c+1
        else:
            break
if c==len(a):
    print("yes")
else:
    print("no")

        
#str cmp
