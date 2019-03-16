s=input()
s=s.replace("a","*")
s=s.replace("b","*")
l=list(s)
if l.count("*")==len(s):
    print("yes")
elif l.count("*")==len(s)-1:
    print("yes")
else:
    print("no")
#only a and b
