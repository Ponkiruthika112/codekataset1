s=input()
k=""
for i in range(0,len(s)):
    if s[i]!="*":
        k=k+s[i]
        s=s.replace(s[i],"*")
print(k)
#remove repeated letters
