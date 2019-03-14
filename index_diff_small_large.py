n=int(input())
l=list(map(int,input().split()))
print(abs(l.index(max(l))-l.index(min(l))))
#index
