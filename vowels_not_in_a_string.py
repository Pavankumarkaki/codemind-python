s=input()
v="aeiou"
b=[]
for i in v:
    if i not in s and i not in b:
        b.append(i)
if len(b)==0:
    print(0)
else:
    print(*b)