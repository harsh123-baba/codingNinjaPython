
def countnum(n):
    if n==0:
        return 0
    if n%10 == 0:
        return 1+countnum(n//10)
    return countnum(n//10)

print(countnum(100020))
    