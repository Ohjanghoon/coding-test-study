def solution(s):
    
    # 테스트 통과 X
    # try:
    #     if len(s) in (4, 6) and int(s):
    #         return True
    #     else:
    #         return False
    # except:
    #     return False

    # .isdigit(): 문자열이 숫자로만 이루어져있는지 확인하는 함수
    # in (): ()의 숫자에 해당하는지 검사
    return s.isdigit() and len(s) in (4, 6)

