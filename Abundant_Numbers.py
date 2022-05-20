def spf(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
n=int(input())
if spf(n)>n:
    print(True)
else:
    print(False)