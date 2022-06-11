s=input()
c,v,d,sp=0,0,0,0
for i in s:
    if i.isalpha():
        if i.lower() in "aeiou":
            v+=1
        else:
            c+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        sp+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",sp)