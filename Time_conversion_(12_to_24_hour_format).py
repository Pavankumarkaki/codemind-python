s=input()
h=int(s[0])*10+int(s[1])
m=int(s[3])*10+int(s[4])
if s[6]=="A":
    if h==12:
        if m==0:
            print("00:0%d"%m)
        else:
            print("00:%d"%m)
    elif h<10:
        if m==0:
            print("0%d:0%d"%(h,m))
        else:
            print("0%d:%d"%(h,m))
    else:
        if m==0:
            print("%d:0%d"%(h,m))
        else:
            print("%d:%d"%(h,m))
        
else:
    if h==12 and s[6]=='P':
        if m==0:
            print("%d:0%d"%(h,m))
        else:
            print("%d:%d"%(h,m))
    elif m==0:
        print("%d:0%d"%(h+12,m))
    else:
        print("%d:%d"%(h+12,m))