def fib(n):
    a,b=0,1
    if n==a or n==b:
        print(True)
    else:
        c=a+b
        a=b
        b=c
        while c<n:
            c=a+b
            a=b
            b=c
        if c==n:
            print(True)
        else:
            print(False)

n=int(input())
fib(n)