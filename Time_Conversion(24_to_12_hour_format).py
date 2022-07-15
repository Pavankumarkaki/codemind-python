s=input()
if(s[0:2]=="00"):
    print("12"+":"+s[3:5],"AM")
elif int(s[0:2])<12:
    print(s[0:2]+":"+s[3:5],"AM")
elif int(s[0:2])==12:
    print(s[0:2]+":"+s[3:5],"PM")
elif int(s[0:2])>12:
    k=int(s[0:2])-12
    if k<10:
        print("0"+str(k)+":"+s[3:5],"PM")
    else:
        print(str(k)+":"+s[3:5],"PM")