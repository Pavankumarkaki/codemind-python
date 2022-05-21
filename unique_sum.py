n=int(input())
l=list(map(int,input().split()))
N=[]
for i in l:
    if i not in N:
        N.append(i)
print(sum(N))