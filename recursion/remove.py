
def removeX(s):
    l =len(s)
    if(l==0):
        return s
    # smallOutput = removeX(s[1:])
    smallOutput = removeX(s[1:])
    if(s[0]=='x'):
        return smallOutput

    else:
        return s[0]+smallOutput;

s = "xaxbx"
print(removeX(s));