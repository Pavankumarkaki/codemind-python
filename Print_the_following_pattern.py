n=int(input())
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
     for j in range(n-i-1):
          print(" ",end="")
     for k in range(i+1):
          print(alpha[k],end="")
     for l in range(i,0,-1):
         print(alpha[l-1],end="")
     print()
