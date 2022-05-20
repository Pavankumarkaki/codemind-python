n=int(input())
l=list(map(int,input().split()))
e=[]
ei,oi=0,0
o=[]
for i in range(n):
    if l[i]%2==0:
        e.insert(ei,l[i])
        ei+=1
    else:
        o.insert(oi,l[i])
        oi+=1
print(*e,end=" ")
print(*o)
    