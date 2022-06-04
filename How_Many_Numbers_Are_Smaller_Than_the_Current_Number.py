n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    c=0
    for j in l:
        if j<i:
            c+=1
    a.append(c)
print(*a)