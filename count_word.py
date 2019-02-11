s=input()
k=input()
c=0
for i in range(0,len(s)):
    if s[i:i+len(k)]==k:
        c=c+1
print(c)

#count
