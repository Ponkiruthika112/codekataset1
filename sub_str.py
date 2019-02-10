s=input()
c=0
k=0
for i in range(0,len(s)-5):
    if s[i:i+6]=="sundar":
        c=c+1
    if s[i:i+6]=="vishal":
        k=k+1
if c!=0 and k!=0:
    print("yes")
else:
    print("no")
#substring
