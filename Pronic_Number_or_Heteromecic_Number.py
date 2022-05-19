def pn(n):
    for i in range(1,n):
        if i*(i+1)==n:
            return True
    else:
        return False
n=int(input())
if pn(n):
    print("YES")
else:
    print("NO")