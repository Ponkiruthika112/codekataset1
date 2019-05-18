# your code goes here
# your code goes here
s=input()
k="dhoni"
if s==k:
	print("no")
elif len(s)==len(k):
	for i in range(0,len(s)):
		if k.count(s[i])!=1:
			break
	if i==len(s)-1:
		print("yes")
	else:
		print("no")
else:
	print("no")
 #anagram
