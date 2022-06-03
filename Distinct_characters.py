s=input()
s=s.lower()
g=[]
for i in s:
    if s.count(i)==1 and i!=" ":
        g.append(i)
g.sort()
print("".join(g))