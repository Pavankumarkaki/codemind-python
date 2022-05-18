def revs(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    return rev
def pali(n):
    if n==revs(n):
        return True
    else:
        return False
    
n=int(input())
n=n+revs(n)
while pali(n)==False:
    n=n+revs(n)
print(n)
