n=int(input())
arr=list(map(int,input().split()))
if n<3:
    print(max(arr));
else:
    arr.sort()
    max=n-1;
    for i in range(2):
        while(arr[max]==arr[max-1]):
            max-=1
        max-=1
    print(arr[max])
        