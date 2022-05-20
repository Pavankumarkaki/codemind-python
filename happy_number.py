def hap(n):
    if n<10:
        return n
    
    s=0
    while n>0:
        s+=(n%10)**2
        n//=10
    return hap(s)
        
n=int(input())
if hap(n)==1 or hap(n)==7:
    print(True)
else:
    print(False)