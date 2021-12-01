n = int(input())
i =1
while i<=n:
    j = n
    while j>=i:
        print("*", end='')
        j-=1
    i+=1
    print()

m = int(input())
i =1
while i<=n:
    j = n
    p=1
    while j>=i:
        print(p, end='')
        p+=1
        j-=1
    i+=1
    print()

m = int(input())
i =1
while i<=n:
    j = n
    p=1
    while j>=i:
        print(p+i-1, end='')
        p+=1
        j-=1
    i+=1
    print()

