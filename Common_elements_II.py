a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
d=[]
for i in m:
    if i not in n and i not in d:
        d.append(i)
for i in n:
    if i not in m and i not in d:
        d.append(i)
print(*d)