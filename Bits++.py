t=int(input())
a=[]
v=0
for i in range(t):
    a.append(input())
for i in a:
    if "+" in i:
        v+=1
    else:
        v-=1
print(v)