def ReplaceChar(s, a, b):
    l =  len(s);
    if l == 0:
        return s

    smallOutput = ReplaceChar(s[1:], a, b)
    if s[0]==a:
        return b+smallOutput
    else:
        return s[0]+smallOutput


print(ReplaceChar("aaabbb", 'a', 'b'))
    