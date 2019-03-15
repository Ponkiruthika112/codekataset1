s=input()
k=""
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        k=k+i
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        s=s.replace(i,"")
print(k+s)
#vowels placwd in front
