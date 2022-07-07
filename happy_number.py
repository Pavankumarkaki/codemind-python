def happy(n):
    if n<=10:
        if n==1 or n==7 or n==10:
            return True
        else:
            return False
    else:
        while n>9:
            s=0
            for i in str(n):
                s+=int(i)**2
            n=s
        if n==1 or n==7:
            return True
        else:
            return False
        
n=int(input())
print(happy(n))