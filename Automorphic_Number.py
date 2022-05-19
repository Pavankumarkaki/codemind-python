n=int(input())
s=str(n*n)
k=int(s[-len(str(n)):])
if n==k:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")