def fib(n):
    a,b=0,1
    if n==0:
        print("0")
    elif n==1:
        print("1")
    else:
        c=a+b
        while c<n:
            a=b
            b=c
            c=a+b
            #print(a,b,c)
        if abs(c-n)==abs((b)-n):
            print(b,c)
        elif abs(c-n)<abs((b)-n):
            print(c)
        else:
            print(b)
            
n=int(input())
fib(n)
#print(n)
