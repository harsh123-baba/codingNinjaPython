def stairCaseHelper(n, count):
    if(n<=0):
        return 0;
    x = 1+stairCaseHelper(n-1, count)
    y = 0
    z = 0
    if(n-2>=0):
        y = 1+ stairCaseHelper(n-2, count) 
    if n-3>=0:
        z = 1+stairCaseHelper(n-3, count)

    count = x+y+z
    return count

def stairCase(n):
    count = 0
    return stairCaseHelper(n, count)

print(stairCase(5))