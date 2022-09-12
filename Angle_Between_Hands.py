h,m=map(int,input().split(":"))
a=abs(30*h-(5.5*m))
aa=360-a
print(min(a,aa))