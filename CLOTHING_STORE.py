n,a=int(input()),list(map(int,input().split()))
a.sort()
c=0
b=set(a)
for i in b:
    if a.count(i)>1:
        c+=a.count(i)//2
print(c)
