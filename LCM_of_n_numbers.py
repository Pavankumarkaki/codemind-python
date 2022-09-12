def LCM(a,b):
    c=max(a,b)
    while True:
        if c%a==0 and c%b==0:
            return c
        c+=1
n=int(input())
a=list(map(int,input().split()))
lcm=LCM(a[0],a[1])
for i in range(2,n):
    lcm=LCM(lcm,a[i])
print(lcm)