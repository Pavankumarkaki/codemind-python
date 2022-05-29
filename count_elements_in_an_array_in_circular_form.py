n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if (l[i-1]%2==0 and l[i+1]%2!=0) or (l[i-1]%2!=0 and l[i+1]%2==0):
        c+=1
if (l[n-2]%2==0 and l[0]%2!=0) or (l[n-2]%2!=0 and l[0]%2==0):
    c+=1
if (l[n-1]%2==0 and l[1]%2!=0) or (l[n-1]%2!=0 and l[1]%2==0):
    c+=1
print(c)