n=int(input())
a=list(map(int,input().split()))
N=[]
c=0
for i in a:
    if i not in N and i%2!=0:
        N.append(i)
        c+=1
print(c)
