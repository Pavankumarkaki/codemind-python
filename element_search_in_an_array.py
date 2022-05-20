n=int(input())
l=list(map(int,input().split()))
s=int(input())
for i in range(n):
    if l[i]==s:
        print(True)
        break
else:
    print(False)