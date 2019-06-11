def check(s):
        l=[]
        if s==s[::-1]:
                l.append(len(s))
        else:
                for i in range(0,len(s)):
                        for j in range(len(s),0,-1):
                                st=s[i:j+1]
                                if st==st[::-1]:
                                        l.append(len(st))
        return l
s=input()
print(max(check(s)))
#h
