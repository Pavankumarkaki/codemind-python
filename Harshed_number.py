def har(m):
    n=m
    s=0
    while n>0:
        s+=n%10
        n//=10
    if m%s==0:
        return True
    return False
m=int(input())
print(har(m))