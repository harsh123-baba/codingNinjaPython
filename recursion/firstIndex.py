def findIndex(a , key, si):
    l = len(a)
    if(key == a[0]):
        return si
    smallList = a[1:]
    return findIndex(smallList, key, si+1)

l = [1, 2, 3, 4 , 5, 5, 5]
print(findIndex(l, 5, 0))