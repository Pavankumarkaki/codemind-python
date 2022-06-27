def isprime(n):
    if n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        else:
            return 1
def pal(n):
    if str(n)==str(n)[::-1]:
       return 1
    else:
        return 0
n=int(input())
n+=1
while(pal(n)==0 or isprime(n)==0):
    n+=1
print(n)