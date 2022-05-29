def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
def pal(n):
    tem=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if tem==rev:
        return True
    else:
        return False
n=int(input())
n+=1
while pal(n)==False or isprime(n)==False:
    n+=1
print(n)