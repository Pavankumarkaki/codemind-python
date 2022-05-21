n=int(input())
l=list(map(int,input().split()))
N=[]
for i in l:
    if i not in N and i%2==0:
        N.append(i)
print(len(N))