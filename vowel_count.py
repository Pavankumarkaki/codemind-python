s=input()
v="aeiouAEIOU"
c=0
for i in range(len(s)):
    if s[i] in v:
        c+=1
print(c)