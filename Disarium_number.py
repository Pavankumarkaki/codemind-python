def dis(n):
    if n<10:
        return True
    else:
        temp=n
        i=len(str(n))
        s=0
        while n>0:
            r=n%10
            s+=r**i
            i-=1
            n//=10
        if s==temp:
            return True
        else:
            return False
            
n=int(input())
print(dis(n))