def revs(n):
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n//=10
    return rev
n=int(input())
if n>0:
    print(revs(n))
else:
    print(-1*revs(abs(n)))