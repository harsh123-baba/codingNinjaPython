# n = int(input())
# n1 = (n+1)/2
# n2 = n-n1

# i=1
# while i<=n1:
#     spaces = 1
#     while(spaces <= n1-i):
#         spaces+=1
#         print(" ", end='')
#     j=1
#     while j<=2*i-1:
#         print("*", end='')
#         j+=1
#     i+=1
#     print()

# i = n2
# while i>=1:
#     spaces = 1;
#     while spaces <= n2-i+1:
#         spaces+=1
#         print(" ", end='')
    
#     j=1
#     while j<=2*i-1:
#         print("*", end='')
#         j+=1
#     i-=1
#     print()



n = int(input())
n1 = (n+1)/2
n2 = n-n1

i = 1
while i<=n1:
    spaces = 1
    while spaces <= n1-i:
        print(" ", end='')
        spaces +=1
    j=1
    while j<=2*i-1:
        print("*", end='')
        j+=1
    print()
    i+=1

i = n2;
while i>=1:
    spaces = 1;
    while spaces <= n2-i-1:
        spaces+=1
        print(" ", end='')
    j=1
    while j<=2*i-1:
        j+=1
        print("*", end='')
    i-=1
    print()




