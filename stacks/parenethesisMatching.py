# # stack
# def Paranthsis(string):
#     s = []
#     for char in string:
#         if char in '({[':
#             s.append(char)
#         elif char == ')':
#             if not s or s[-1]!='(':
#                 return False
#             else:
#                 s.pop()
#         elif char== '}':
#             if not s or s[-1]!='{':
#                 return False

#             else:
#                 s.pop()
        
#         elif char ==']':
#             if not s or s[-1]!='[':
#                 return False
#             else:
#                 s.pop()
#     if not s:
#         return True
#     else:
#         return False           
# string = input()
# print(Paranthsis(string))

def parentheisPrac(string):
    s = []
    for char in string:
        if char in '([{':
            s.append(char)

        elif char == ')':
            if not s or s[-1] != '(':
                return False
            else:
                s.pop()

        elif char == '}':
            if not s or s[-1] != '{':
                return False
            else:
                s.pop()

        elif char == ']':
            if not s or s[-1]!='[':
                return False
            else:
                s.pop()
    if not s:
        return True

    else:
        return False

string = input()
print(parentheisPrac(string))






























