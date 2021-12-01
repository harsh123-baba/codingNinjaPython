def BinarySearch(l, low, high, key):
    if(low>high):
        return -1
    mid = (low+high)//2
    if(key == l[mid]):
        return mid
    
    elif(l[mid] < key):
        return BinarySearch(l, mid+1, high, key)
    else:
        return BinarySearch(l, low, mid-1, key)
    
l = [1, 2,3, 4, 5, 6, 7]
print(BinarySearch(l, 0, 6, 3))