n=int(input())
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=""
while n>0:
    r=n%26
    if r==0:
        s+='Z'
        n=(n//26)-1
    else:
        s+=a[r-1]
        n=n//26
print(s[::-1])