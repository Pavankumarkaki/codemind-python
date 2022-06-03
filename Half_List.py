n=int(input())
a=list(map(int,input().split()))
for i in range(n-1,(n//2)-1,-1):
    print(a[i],end=" ")
print(*a[0:n//2:1],end=" ")