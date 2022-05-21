n=int(input())
l=list(map(int,input().split()))
N=[]
s=0
for i in l:
    if i not in N and i%2!=0:
        N.append(i)
        s+=i
print(s)