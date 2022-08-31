n,m=map(int,input().split())
a=[]
c=0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in a:
    k=i.copy()
    k.sort()
    if k==i:
        c+=1
    k.reverse()
    if k==i:
        c+=1
print(c)