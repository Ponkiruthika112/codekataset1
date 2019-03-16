s=input()
c=0
l=["a","e","i","o","u"]
for i in range(0,len(s)-2):
    if l.count(s[i])==1 and l.count(s[i+1])==0:
        c=c+2
        if l.count(s[i+1])==0 and l.count(s[i+2])==1:
            c=c+1
print(c)
#alternate vowels and consonants
