n=int(input())
l=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if i%2==0:
        es+=l[i]
    else:
        os+=l[i]
print(abs(es-os))