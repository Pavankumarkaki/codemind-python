s=input()
u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=0
for i in s:
    if i in u:
        c+=1
print(c)