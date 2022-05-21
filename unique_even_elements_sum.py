n=int(input())
l=list(map(int,input().split()))
s=0
N=[]
for i in l:
    if i not in  N and i%2==0:
        N.append(i)
        s+=i
print(s)