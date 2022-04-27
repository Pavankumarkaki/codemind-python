n=int(input())
d=n*n
sum=0
while d>0:
    r=d%10
    sum+=r
    d=d//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')