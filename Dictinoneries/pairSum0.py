def pairSum(a):
    d = {}
    i = 0;
    for i in range(len(a)):
        if 0-a[i] in d:
            return True

        else:
            d[a[i]]=1;
    return False


a = [1, 3, 4, 45];
print(pairSum(a))
