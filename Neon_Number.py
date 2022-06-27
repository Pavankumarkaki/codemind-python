def neon(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
n=int(input())
s=n*n
if n==neon(s):
    print("Neon Number")
else:
    print("Not Neon Number")