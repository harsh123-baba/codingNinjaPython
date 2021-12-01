def partition(A, si, ei):
    pivot = A[si]
    
    # get the smaller elements
    c = 0
    for i in range(si, ei+1):
        if A[i] < pivot :
            c+=1;
    A[si], A[si+c] = A[si+c] , A[si];
    pivotIndex = si+c
    i = si;
    j = ei;
    while i<j:
        if A[i] < pivot:
            i+=1
        elif A[j] > pivot:
            j-=1
        else:
            A[i] , A[j] = A[j], A[i];
            i+=1;
            j+=1
    return pivotIndex      








def quickSort(A, si, ei):
    if si>= ei:
        return 
    pivotIndex = partition(A, si, ei)
    quickSort(A, si, pivotIndex-1)
    quickSort(A, pivotIndex+1, ei)

l = [10, 5, 6, 2, 3, 9, 4]
quickSort(l, 0, 6);
for i in range(len(l)):
    print(l[i])

