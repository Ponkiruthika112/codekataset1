import math
n=int(input())
r=math.radians(n)
if n==90:
    print(1)
else:
    print(round(math.sin(r),1))
#sin
