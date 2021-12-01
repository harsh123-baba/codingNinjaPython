n = int(input())
i=1
while i<=n:
    spaces = 1
    while spaces <= n-i:
        print(" ", end='')
        spaces+=1
    j=1
    while j<=i:
        print("*", end='')
        j+=1
    p=1
    while p<=i-1:
        print("*", end='')
        p+=1
    i+=1
    print()



