def solution(s, n):
    answer = ''
    
    
    for alpha in s:
        if alpha == ' ':
            answer += ' '
        else:
            if alpha.isupper():
                answer += chr((ord(alpha) - ord('A') + n) % 26 + ord('A'))
            else:
                answer += chr((ord(alpha) - ord('a') + n) % 26 + ord('a'))
                
    return answer