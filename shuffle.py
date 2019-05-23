s=input()
c=0
if len(s)==1:
    print("yes")
else:
    for i in s:
        if s.count(i)==len(s):
            print("no")
            c=1
            break
    if c==0:
        print("yes")
#rep
