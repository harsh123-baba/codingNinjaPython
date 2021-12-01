# ABCD
# ABCD
# ABCD
# ABCD

n = int(input())
i = 0
while i<n:
    j = 0
    while j<n:
        print(chr(ord('A')+j), end='')
        j+=1
    i+=1
    print()

# ABCD
# BCDE
# CDEF
# DEFG

n = int(input())
i = 1
while i<=n:
    j = 1
    p = i
    while j<=n:
        x = ord('A')+p-1
        p+=1
        print(chr(x), end='')
        j+=1
    i+=1
    print()


# Tringle
n = int(input())
i = 1
while i<=n:
    j = 1
    p=i
    while j <=i:
        x = ord('A')+p-1
        print(chr(x), end='')
        p+=1
        j+=1
    i+=1
    print()

