def sd(n):
    t=n
    while n>0:
        r=n%10
        if r==0 or t%r!=0:
            return False
        n//=10
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if sd(i):
        print(i,end=" ")