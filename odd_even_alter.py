s=input()
e=0
o=0
for i in s:
    if int(i)%2==0:
        e=e+1
    else:
        o=o+1
if e==0 or o==0:
    print(0)
elif e==o:
    print(e+o)
else:
    print(abs(e-o))
#alter odd even
