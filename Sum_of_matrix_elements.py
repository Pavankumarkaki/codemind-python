m=int(input())
n=int(input())
a={}
for i in range(m):
    a[i]=sum(list(map(int,input().split())))
s=0
for i in a.values():
    s+=i
print(s)