n,l=int(input()),list(map(int,input().split()))
b=[]
for i in l:
    if l.count(i)==1:
        b.append(i)
if len(b)!=0:
    print(*b)
else:
    print(-1)