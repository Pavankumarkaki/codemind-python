t=int(input())
while t>0:
    c=input()
    for i in c:
        if i.isdigit():
            print("Yes")
            break
    else:
        print("No")
    t-=1