n = int(input())
i = 1
while i<=n:
    j = n
    while j>=1:
        if j>i:    
            print(" ", end='')
        else:
            print("*", end="")
        j-=1

    i+=1
    print()

m = int(input())
i = 1
while i<=n:
    j = n
    p = 1
    while j>=1:
        if(j>i):
            print(" ", end='')
        else:
            print(p, end="")
            p+=1    
        j-=1
    i+=1
    print()


m = int(input())
i = 1
while i<=n:
    j = n
    p = 1
    while j>=1:
        if(j>i):
            print(" ", end='')
        else:
            print(p+i-1, end="")
            p+=1    
        j-=1
    i+=1
    print()

# /***************** or *************************/
l = int(input())
i = 1
while i <=l:
    spaces = 1
    while spaces <= n-i:
        print(" ", end='')
        spaces+=1
    p=1
    j=1
    while j <= i:
        print(p, end='')
        p+=1
        j+=1
    print()
    i+=1
