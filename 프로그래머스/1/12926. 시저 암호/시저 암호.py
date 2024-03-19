def solution(s, n):
    answer = ''
    upper_alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    lower_alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    # 2. list index 활용
    for alpha in s:
        if alpha == ' ':
            answer += ' '
        else:
            if alpha.isupper():
                idx = (upper_alpha.index(alpha) + n) % 26
                answer += upper_alpha[idx]
            else:
                idx = (lower_alpha.index(alpha) + n) % 26
                answer += lower_alpha[idx]
    
    # 1. ord 활용 풀이
    # for alpha in s:
    #     if alpha == ' ':
    #         answer += ' '
    #     else:
    #         if alpha.isupper():
    #             answer += chr((ord(alpha) - ord('A') + n) % 26 + ord('A'))
    #         else:
    #             answer += chr((ord(alpha) - ord('a') + n) % 26 + ord('a'))
                
    return answer