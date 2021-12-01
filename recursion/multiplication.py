def mul(a, b):
    if(a == 0 ):
        return 0;
    if a ==1:
        return b
    return b + mul(a-1, b);

print(mul(3, 5))