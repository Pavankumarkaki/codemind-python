def ds(n):
    s=0
    i=len(str(n))
    while n>0:
        r=n%10
        s+=r**i
        i-=1
        n//=10
    return s
n=int(input())
if ds(n)==n:
    print(True)
else:
    print(False)