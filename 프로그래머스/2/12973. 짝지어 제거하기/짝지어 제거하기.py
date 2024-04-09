def solution(s):
    stack = []
    for alpha in s:
        if len(stack) > 0 and stack[-1] == alpha:
            stack.pop(-1)
            continue
        else:
            stack.append(alpha)
            

    return 1 if len(stack) == 0 else 0