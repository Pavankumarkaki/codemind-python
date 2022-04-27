import math
p,r,t=map(int,input().split())
i=p*math.pow(1+r/100.0,t)
print("{:.2f}".format(i))