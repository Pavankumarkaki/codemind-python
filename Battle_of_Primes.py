def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input())
m=int(input())
i=1
while not isprime(i+n+m):
    i+=1
print(i)