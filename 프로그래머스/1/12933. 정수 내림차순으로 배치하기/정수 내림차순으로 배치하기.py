def solution(n):
    tmp = list(str(n))
    tmp.sort(reverse = True)
    
    # '{합쳐질 원소간 넣고 싶은 문자열}'.join(<리스트>)
    answer = int(''.join(tmp))
    return answer