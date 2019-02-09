n=int(input())
for i in range(2,n):
    if n%i==0:
        print("yes")
        break
    elif i==n-1:
        print("no")
#finding a no div 
