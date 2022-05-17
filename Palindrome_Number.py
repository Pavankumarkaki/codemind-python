def pal(n):
    rev=0
    temp=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    if rev==temp:
        return True
    return False
t=int(input())
while t>0:
    n=int(input())
    if pal(n) and n>0:
        print("True")
    else:
        print("False")
    t-=1