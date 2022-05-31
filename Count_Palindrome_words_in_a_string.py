def pal(s):
    ss=s[::-1]
    if s.lower()==ss.lower():
        return True
    else:
        return False
s=input()
l=s.split(" ")
c=0
for i in l:
    if pal(i):
        c+=1
print(c)