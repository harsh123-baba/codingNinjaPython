# 1
# 11
# 111
# 1111

n = int(input())
i=1
while i<=n:
    j = 1
    while j<=i:
        print(1, end='')
        j+=1
    i+=1
    print()

# 1
# 23
# 345
# 4567

m = int(input())
i = 1
while i<=n:
    j = 1
    p = i
    while j<=i:
        print(p, end='')
        p+=1
        j+=1
    i+=1
    print()

# 1
# 23
# 456
# 78910

m =int(input())
i = 1
p =1
while i<n:
    j = 1
    while j<=i:
        j+=1
        print(p, end='')
        p+=1
    i+=1
    print()






