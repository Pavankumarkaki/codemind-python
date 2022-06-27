n=int(input())
a=list(map(int,str(n)[::]))
s=set(a)
if len(a)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")