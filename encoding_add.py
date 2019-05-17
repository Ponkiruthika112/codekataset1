# your code goes here
a=input()
b=input()
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s=""
for i in range(0,len(a)):
	x=l.index(a[i])+1
	y=l.index(b[i])+1
	s=s+l[((x+y)%26)-1]
print(s)
#encoding
