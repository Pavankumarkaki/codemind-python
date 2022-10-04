n=int(input())
arr=list(map(int,input().split()))
uniq=[]
for i in arr:
    if arr.count(i)==1:
        uniq.append(i)
if len(uniq)==0:
    print(-1)
else:
    print(max(uniq))