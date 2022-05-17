def pretty(n):
    r=n%10
    if r==2 or r==3 or r==9:
        return True
    else:
        return False
t=int(input())
while t>0:
    a,b=map(int,input().split())
    c=0
    for i in range (a,b+1):
        if pretty(i):
            c+=1
    print(c)
    t-=1