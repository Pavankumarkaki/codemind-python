a=list(map(int,input().split()))
b=list(map(int,input().split()))
aa=0
bb=0
for i in range(3):
    if a[i]>b[i]:
        aa+=1
    elif a[i]<b[i]:
        bb+=1
print(aa,bb)