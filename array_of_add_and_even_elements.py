n=int(input())
l=list(map(int,input().split()))
e=0
o=0
ee=[]
oo=[]
for i in range(n):
    if l[i]%2==0:
        ee.append(l[i])
        e+=1
    else:
        oo.append(l[i])
        o+=1
print(*oo,end=" ")
print(*ee)