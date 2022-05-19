def isprime(m):
     if m==1:
          return False
     else:
          for i in range(2,int(m**0.5)+1):
               if m%i==0:
                    return False
          else:
               return True
n=int(input())
m=int(input())
t=n+m
i=1
while not isprime(t+i):
    i+=1
print(i)
