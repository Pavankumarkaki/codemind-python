n=int(input())
arr=list(map(int,input().split()))
output=[1,1,1,1]
for i in range(n):
    for j in range(n):
        if(i==j):
            continue
        else:
            output[i]*=arr[j];
print(*output)