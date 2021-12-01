def isSorted(n):
    l = len(n);
    if l ==0  or l==1:
        return True;

    if n[0] > n[1]:
        return False
    smallList = n[1:]
    return  isSorted(smallList)

l = [1, 2, 3, 40, 5,6];
print(isSorted(l))

