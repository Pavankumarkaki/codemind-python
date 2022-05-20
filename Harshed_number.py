def sd(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n//=10
    return s
n=int(input())
if n%sd(n)==0:
    print(True)
else:
    print(False)