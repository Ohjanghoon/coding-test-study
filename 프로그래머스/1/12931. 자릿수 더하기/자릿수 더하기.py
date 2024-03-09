def solution(n):
    answer = 0
    
    str_n = str(n)
    for n in str_n:
        answer += int(n)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer