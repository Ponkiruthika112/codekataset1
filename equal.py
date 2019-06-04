a,b=map(str,input().split("|"))
c=input()
if len(a)==len(b)+len(c):
	print(a+"|"+b+c)
elif len(a)+len(c)==len(b):
	print(a+c+"|"+b)
else:
	print("impossible")
#HJK
