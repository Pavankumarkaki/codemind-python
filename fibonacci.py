def fib(n):
    a,b=0,1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(3,n+1):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
n=int(input())
fib(n)