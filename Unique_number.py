n=input()
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i]==n[j] and i!=j:
            print("Not Unique Number")
            exit()
else:
    print("Unique Number")