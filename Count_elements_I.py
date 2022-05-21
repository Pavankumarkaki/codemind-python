a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
c=0
N=[]
for i in m:
    if i not in N:
        N.append(i)
for i in N:
    if i in n:
        c+=1
print(c)