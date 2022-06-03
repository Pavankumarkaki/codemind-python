def ps(n):
    s=int(n**0.5)
    if s*s==n:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if ps(i):
        s+=i
print(s)
    