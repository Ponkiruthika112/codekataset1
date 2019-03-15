s=input()
k=0
for i in s:
    if i.isdigit():
        k=k+1
    elif i=="A" or i=="B" or i=="C" or i=="D" or i=="E" or i=="F":
        k=k+1
    else:
        break
if k==len(s):
    print("yes")
else:
    print("no")
#check the given hexadecimal
