n = int(input())
i = 2
print(1)
while i<=n:
    j =1
    while j <=i:
        if j == 1 or j==i:
            print(1, end='')

        else:
            print(2, end='')
        j+=1
    i+=1
    print()