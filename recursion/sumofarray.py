def sumArray(n):
    l = len(n)
    if(l == 1):
        return n[0]
    small = n[1:]
    return n[0]+sumArray(small)

l = [1, 2, 3, 4];
print(sumArray(l))