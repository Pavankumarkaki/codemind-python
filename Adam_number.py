def revs(n):
    r=0
    while n>0:
        r=r*10+n%10
        n//=10
    return r
n=int(input())
rn=revs(n)
if n**2==revs(rn**2):
    print(True)
else:
    print(False)