s=input()
a="0123456789"
sm=0
for i in s:
    if i in a:
        sm+=int(i)
print(sm)