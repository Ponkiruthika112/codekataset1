s=input()
for i in range(len(s)-1,-1,-1):
        k=s[0:i+1]
        if k!=k[::-1]:
                print(k)
                break
#not palindrome
