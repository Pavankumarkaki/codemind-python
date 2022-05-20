n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l[i]!=0 and l[i]!=1:
        print(False)
        break
else:
    print(True)