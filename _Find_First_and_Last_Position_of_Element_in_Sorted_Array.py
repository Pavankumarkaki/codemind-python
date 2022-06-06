n=int(input())
a=list(map(int,input().split()))
s=int(input())
if s in a:
    k=a.index(s)
    print(k,end=" ")
    for i in range(n):
        if a[i]==s:
            p=i
    print(p)
else:
    print(-1,-1)