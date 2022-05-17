def sr(n):
    s=int(n**0.5)
    if s*s==n:
        print("True")
    else:
        print("False")
t=int(input())
while t>0:
    n=int(input())
    sr(n)
    t-=1