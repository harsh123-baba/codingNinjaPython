n = int(input())

i =1
while i<=n:
    spaces = 1
    while spaces <= n-i:
        spaces +=1
        print(" ", end='')
    j = 1;
    p = i
    while j<=i:
        print(p, end='')
        j+=1
        p+=1
    p = 2*i-2;
    while p > i-1:
        print(p, end='')
        p-=1
    i+=1;
    print()
