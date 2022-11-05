n=int(input())
alpha="@ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n,0,-1):
    for j in range(i):
        print(alpha[i],end=" ")
    print()