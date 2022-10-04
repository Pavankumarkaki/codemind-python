s=int(input())
start=list(map(int,input().split()))
e=int(input())
end=list(map(int,input().split()))
q=int(input())
c=0
for i in range(s):
    if q>=start[i] and q<=end[i]:
        c+=1
print(c)