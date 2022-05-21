n=int(input())
l=list(map(int,input().split()))
N=[]
for i in l:
    N.append(len(str(abs(i))))
print(*N)
#print(l)