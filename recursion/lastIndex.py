def lastIndex(a, key):
    l = len(a)
    if(l==0):
        return -1
    if key == a[l-1]:
        return l-1
    smallList = a[:l-1]
    return lastIndex(smallList, key)

l = [1, 2,3,4, 5, 5, 5, 6]
print(lastIndex(l, 5))


# USING FIRST IDEX METHOD

def lastIndexFirstIndex(a, key):
    l = len(a)
    if l ==0 :
        return -1

    small = a[1:];
    smallerOutput = lastIndexFirstIndex(small, key)
    if(smallerOutput != -1):
        return smallerOutput+1;
    else:
        if a[0] == key:
            return 0;
        else:
            return -1;


l = [1, 2,3,4, 5, 5, 5, 6]
print(lastIndex(l, 5))
