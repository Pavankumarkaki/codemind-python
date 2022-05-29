s=input()
d="0123456789 "
a="abcdefghijklmnopqrstuvwxyz"
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=0
for i in s:
    if i not in d and i not in a and i not in A:
        c+=1
print(c)
#print(s)