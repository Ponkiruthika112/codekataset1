def count(i):
    c=0
    k=str(i)
    c=c+k.count("2")
    return c
n=int(input())
j=0
for i in range(2,n+1):
    j=j+count(i)
print(j)
#cnt2
