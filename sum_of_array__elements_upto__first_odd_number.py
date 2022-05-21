n=int(input())
l=list(map(int,input().split()))
s=0
i=0
while i<n:
    if l[i]%2!=0:
        break
    else:
        s+=l[i]
        i+=1
print(s)