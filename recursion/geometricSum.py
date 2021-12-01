def power(n, k):
    if k ==0:
        return 1;
    if k==1:
        return n;
    return n*power(n, k-1);


def gs(k):
    if k == 0:
        return 1
    
    return 1/pow(2, k) + gs(k-1)

# print(power(2, 3))
print(gs(3))
    