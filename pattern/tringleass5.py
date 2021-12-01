n = int(input())
i = 1
while i<=n:
    
    j =1
    x = ord('A')+i-1
    while j<=i:
        print(chr(x), end='')
        j+=1
    i+=1
    print()
