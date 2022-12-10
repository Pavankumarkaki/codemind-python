def isbal(s):
    stk=[]
    for i in s:
        if i in ['(','[','{']:
            stk.append(i)
        else:
            if len(stk)==0:
                return False
            else:
                if i==')' and stk[-1]!='(':
                    return False
                if i=='}' and stk[-1]!='{':
                    return False
                if i==']' and stk[-1]!='[':
                    return False
                stk.pop()
    return True if len(stk)==0 else False
s=input()
print(isbal(s))