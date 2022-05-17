def revs(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    return rev
n=int(input())
nn=revs(n)
if n**2==revs(nn**2):
    print(True)
else:
    print(False)