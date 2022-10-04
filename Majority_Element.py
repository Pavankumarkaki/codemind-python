n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    if arr.count(i)>n/2:
        print(i)
        exit()