n=int(input())
rev=0
nn=n
n=abs(n)
while n>0:
    r=n%10
    rev=rev*10+r
    n//=10
if nn>0:
    print(rev)
else:
    print(-1*rev)