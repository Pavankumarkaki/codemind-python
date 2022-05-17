m=int(input())
rev=0
while m>0:
    rev=rev*10+m%10
    m//=10
print(rev)
    