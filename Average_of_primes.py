def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input())
l=list(map(int,input().split()))
N=[]
for i in l:
    if isprime(i):
        N.append(i)
print("{:.2f}".format(sum(N)/len(N)))