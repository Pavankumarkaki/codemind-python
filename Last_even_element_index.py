n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l[i]%2==0:
        e=i
print(e)