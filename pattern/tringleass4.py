n = int(input())
i = 1
while i <=n:
    j = n
    p = 1
    while j>=i:
        print(p, end='')
        p=p+1
        j-=1
    i+=1
    print()