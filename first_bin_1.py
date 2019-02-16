n=int(input())
s=bin(n)[2:]
c=0
for i in range(len(s)-1,0,-1):
    if s[i]=="1":
        print(2**c)
        break
    c=c+1

#first bin
