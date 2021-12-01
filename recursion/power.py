# def power(n, x):
#     if(x==0):
#         return 1
#     if x==1:
#         return n

#     return n*power(n, x-1)
# n = input("Enter number : ")
# x= input("enter power val ")
# print(power(n, x))

# optimized

def powOptimized(n, x):
    if(x==0):
        return 1;
    if x==1:
        return n

    if x%2 == 0:
        return powOptimized(n*n, x/2)
    else:
        return n* powOptimized(n*n, x/2)
    


print(powOptimized(2 , 9))