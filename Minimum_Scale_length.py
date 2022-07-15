def hcf(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
n=int(input())
l=list(map(int,input().split()))
h=hcf(l[0],l[1])
for i in range(2,n):
    h=hcf(h,l[i])
print(h)