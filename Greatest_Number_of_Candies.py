n=int(input())
l=list(map(int,input().split()))
e=int(input())
for i in l:
    k=i+e
    if max(l)<=k:
        print(True,end=" ")
    else:
        print(False,end=" ")