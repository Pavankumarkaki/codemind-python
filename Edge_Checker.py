a,b=map(int,input().split())
if (a==1 and b==10) or(a==10 and b==1):
    print("Yes")
elif a<10 and b<10:
    if a==b+1 or b==a+1:
        print("Yes")
    else:
        print("No")
else:
    print("No")

    