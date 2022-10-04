n=int(input())
res=""
a="ZABCDEFGHIJKLMNOPQRSTUVWXY"
while(n>0):
     R=n%26
     if R==0:
          res+='Z'
          n=n//26-1
     else:
          res+=a[R]
          n//=26
print(res[::-1])
