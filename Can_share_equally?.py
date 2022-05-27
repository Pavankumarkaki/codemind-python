a,b=map(int,input().split())
t=a+(b*2)
#print(a,b)
if t%2==0 and t>0:
    if a%2==0 and b%2==0:
        print("YES")
    elif a==0 and b%2!=0:
        print("NO")
    elif a%2==0 and (b*2)%2==0: 
        print("YES")
    else:
        print("NO")
else:
    print("NO")