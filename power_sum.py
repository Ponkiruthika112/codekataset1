n=int(input())
s=str(n)
c=0
for i in range(0,len(s)-1):
    c=c+int(s[i])**int(s[i+1])
c=c+int(s[-1])**int(s[0])
print(c)
#power
