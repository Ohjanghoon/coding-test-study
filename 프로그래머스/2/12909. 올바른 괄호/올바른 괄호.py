def solution(s):
    # 2차 시도(스택 활용)
    stack = []
    
    for symbol in s:
        stack.append(symbol)
        if len(stack) >= 2:
            if stack[-2] == "(" and stack[-1] == ")":
                stack.pop(-2)
                stack.pop(-1)
    
    if len(stack) == 0:
        return True
    else:
        return False
    
    
    # 1차 시도(효율성1 시간초과)
#     open_count = s.count("(")
#     close_count = s.count(")")
    
#     if open_count != close_count:
#         return False
#     else:
#         if "()" not in s:
#             return False
#         else:
#             while True:
#                 s = s.replace("()", "")
#                 if "()" not in s:
#                     break
                    
#         if s == "":
#             return True
#         else:  
#             return False