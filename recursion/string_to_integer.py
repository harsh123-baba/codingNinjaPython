
def num(s, integer):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        integer = integer*10+int(s);
        return integer
    smallans = num(s[1:], integer)
    integer = integer*10 + int(s)
    return integer


def stringToInt(s):
    integer = 0
    return num(s, integer)

s = "1001000"
print(stringToInt(s))