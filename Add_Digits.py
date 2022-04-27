a=int(input())
while a>9:
    su=0
    while a>0:
        r=a%10;
        su+=r
        a=a//10
    a=su
print(a)