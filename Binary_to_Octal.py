for i in range(int(input())):
    n=input()
    n="0b"+n
    n=eval(n)
    print(oct(n)[2:])