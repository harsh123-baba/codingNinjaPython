def merge(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge(L)
        merge(R)
        i = j = k = 0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i];
                i+=1

            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1

l = [11, 3, 7, 2 , 1, 9, 4, 5];
merge(l);
for i in range(len(l)):
    print(l[i])
