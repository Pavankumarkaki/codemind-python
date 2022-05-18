def pali(n):
    m=n
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    if rev==m:
        return True
    else:
        return False
n=int(input())
i=n+1
j=n-1
while pali(i)==False:
    i+=1
while pali(j)==False:
    j-=1
if abs(i-n)==abs(n-j):
    print(j,i)
else:
    if abs(i-n)>abs(n-j):
        print(j)
    else:
        print(i)