def maxi(arr,l,h):
    m=-1
    for i in range(l,h):
        if(arr[i]>m):
            m=arr[i];
    return m
    
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    arr[i]=maxi(arr,i+1,n)
print(*arr)
