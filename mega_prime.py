def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input())
if isprime(n):
    while n>0:
        r=n%10
        if not isprime(r):
            print("Not Mega Prime")
            break
        n//=10
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")