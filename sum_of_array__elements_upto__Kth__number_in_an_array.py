n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
for i in range(k):
    s+=l[i]
print(s)