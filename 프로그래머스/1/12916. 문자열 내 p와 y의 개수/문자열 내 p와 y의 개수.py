def solution(s):
    # 문자열을 소문자로 변환
    s = s.lower()
    print(s)
    
    answer = True if s.count('p') == s.count('y') else False
    return answer