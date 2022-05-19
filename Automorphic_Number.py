n=int(input())
s=str(n*n)
if n==int(s[-len(str(n)):]):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")