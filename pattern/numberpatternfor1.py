# three steps to follow 
# 1 . no of rows?
# 2 . no of columns means in which row what no of columns should print
# 3 . what to print in which columns





# 1111
# 1111
# 1111
# 1111

n = int(input())
i = 0;
while(i<n):
    j = 0
    while j < n:
        print(1, end = '')
        j+=1
    i+=1
    print()

# 1234
# 2345
# 3456
# 4567

m = int(input())
i = 1
while(i <= n):
    j = 1
    p = i
    while j<=n:
        print(p, end='')
        p=p+1
        j = j+1

    i=i+1
    print()

# 1234
# 5678
# 9101112

l = int(input())
i = 1
p = 1
while i <= n:
    j = 1
    while j<=n:
        print(p, end='')
        p = p+1
        j +=1
    i+=1
    print()

