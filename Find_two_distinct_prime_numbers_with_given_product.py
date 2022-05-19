def ip(m):
     if m==1:
          return False
     else:
          for i in range(2,int(m**0.5)+1):
               if m%i==0:
                    return False
          else:
               return True
n=int(input())
for i in range(2,n+1):
    for j in range(2,n+1):
        if ip(i) and ip(j) and i*j==n:
            print(i,j)
            exit()
else:
    print(-1)