s=input()
c=s.count("0")
f=0
if s==s[::-1]:
    f=1
else:
    for i in range(c):
        s="0"+s
        if s==s[::-1]:
            f=1
            break
if f==0:
    print("no")
else:
    print("yes")
#q
