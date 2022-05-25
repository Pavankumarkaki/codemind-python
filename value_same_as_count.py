n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i not in b and a.count(i)==i:
     c+=1
     b.append(i)
print(c)