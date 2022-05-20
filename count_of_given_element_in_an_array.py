n=int(input())
l=list(map(int,input().split()))
e=int(input())
c=0
for i in range(n):
    if l[i]==e:
        c+=1
print(c)