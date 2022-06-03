n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
t=int(input())
c=0
for i in l:
    if i>t:
        c+=2
    else:
        c+=1
print(c)