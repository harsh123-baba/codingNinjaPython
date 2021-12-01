def helper(s, start, end):
    if start >= end:
        return True;
    if s[start]!=s[end]:
        return False
    return helper(s, start+1, end-1);


def isPillindrome(s):
    start = 0;
    end = len(s)-1;
    return helper(s, start, end)

s = "is"
print(isPillindrome(s))
