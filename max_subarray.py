def subarray(s):
    l=[" "]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            l.append(s[i:j])
    return l
a=input()
b=input()
x=subarray(a)
y=subarray(b)
d=[]
for i in x:
    if y.count(i)!=0:
        d.append([len(i),i])
d.sort(reverse=True)
print(d[0][1])
        
#subarray
