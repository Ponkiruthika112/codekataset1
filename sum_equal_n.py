def digits(n):
    s=list(str(n))
    c=0
    for i in range(0,len(s)):
        c=c+int(s[i])
    return c
n=int(input())
p=n%9
if p==0:
    print(n//9*"9")
else:
    print(str(digits(n))+n//9*"9")
#sum
