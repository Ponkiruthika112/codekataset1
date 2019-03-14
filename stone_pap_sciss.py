a,b=map(str,input().split())
l=["P","S","R"]
if a=="P" and b=="R" or a=="R" and b=="P":
    print("p")
elif a==b:
    print("D")
else:
    print(l[max(l.index(a),l.index(b))])
      
#STONE PAPER SCISSOR
