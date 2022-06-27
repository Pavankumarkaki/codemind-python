def add(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
while(n>10):
    n=add(n)
print(n)