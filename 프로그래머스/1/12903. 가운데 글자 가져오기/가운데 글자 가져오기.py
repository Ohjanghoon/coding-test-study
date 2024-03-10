def solution(s):
    answer = ''
    middle_idx = int(len(s) / 2)
    
    if len(s) % 2 == 0:
        answer = s[(middle_idx - 1)] + s[middle_idx]
    else:
        answer = s[middle_idx]
    return answer