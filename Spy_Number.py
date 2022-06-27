def spy(n):
    s,p=0,1
    while n>0:
        r=n%10
        s+=r
        p*=r
        n//=10
    if s==p:
        return True
    return False
n=int(input())
if spy(n):
    print("Spy Number")
else:
    print("Not Spy Number")