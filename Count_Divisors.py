i,r,k=map(int,input().split())
count=0
for j in range (i,r+1):
    if(j%k==0):
        count+=1
print(count)