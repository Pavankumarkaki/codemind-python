t=int(input())
j=1
while j<=t:
    n=int(input())
    f=1
    for i in range(n,1,-1):
        f*=i
    print(int(f))
    j+=1