n=int(input())
l=list(map(int,input().split()))
es,os=0,0
for i in range(n):
    if l[i]%2==0:
        es+=l[i]
    else:
        os+=l[i]
print(abs(es-os))