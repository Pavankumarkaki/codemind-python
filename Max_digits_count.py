def digit(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c
n=int(input())
m=list(map(int,input().split()))
f=digit(max(m))
c=0
for i in m:
    if digit(i)==f:
        c+=1
print(c)