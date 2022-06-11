t=int(input())
while t:
    s=input()
    if s==s[::-1]:
        print("YES",end=" ")
        if len(s)%2==0:
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")
    t-=1