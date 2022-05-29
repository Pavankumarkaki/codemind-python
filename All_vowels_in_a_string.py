s=input()
v="aeoiu"
b=[]
for i in s:
    if i in v and i not in b:
        b.append(i)
if len(v)==len(b):
    print(True)
else:
    print(False)