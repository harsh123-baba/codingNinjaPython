def checkAB(s):
    if len(s) == 0:
        return True
    
    if len(s) == 1:
        return True

    if not(s[0] =='b' and s[1]=='a') or not(s[0]=='a' and (s[1]=='b' and s[2] == 'b')):
        return False

    
    return checkAB(s[1:])

print(checkAB("abba"))




