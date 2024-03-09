def solution(n):
    answer = 0
    tmp = [i for i in str(n)]
    tmp = sorted(tmp, reverse = True)
    
    
    # '{합쳐질 원소간 넣고 싶은 문자열}'.join(<리스트>)
    answer = int(''.join(tmp))
    return answer