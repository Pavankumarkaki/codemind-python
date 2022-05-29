s=input()
v="aeiouAEIOU"
b=[]
for i in s:
    if i in v and i not in b:
        b.append(i)
print(*b)