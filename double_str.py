s=input()
if len(s)%2!=0:
    k=len(s)//2
    if s[0:k]==s[k+1::]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
#double string
