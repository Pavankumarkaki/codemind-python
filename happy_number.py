def hap(n):
    s=0
    while n>0:
        r=n%10
        s+=r**2
        n//=10
    return s
n=int(input())
while hap(n)>9:
    n=hap(n)
if hap(n)==1 or hap(n)==7:
    print(True)
else:
    print(False)
    
    