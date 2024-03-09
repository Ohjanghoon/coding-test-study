def solution(num):
    answer = 0
    
    if num == 1: return 0

    while True:
        answer += 1
        # 1-1. 짝수면 2로 나눈다.
        if num % 2 == 0:
            num /= 2
        # 1-2. 홀수라면 3을 곱하고 1을 더한다.
        else:
            num = num * 3 + 1
            
        if num == 1:
            break
        if answer == 500:
            answer = -1
            break
            
        
    return answer