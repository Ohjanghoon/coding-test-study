def solution(left, right):
    answer = 0
    
    # left 수 부터 right 수 까지의 범위 찾기
    for num in range(left, right + 1):
        # 공약수 구하기(제곱근 활용)
        common_divisor = []
        
        for i in range(1, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                common_divisor.append(i)
                if i < num // i:
                    common_divisor.append(num // i)
        
        # 약수의 개수가 짝수면 더하기, 홀수면 빼기
        answer += num if len(common_divisor) % 2 == 0 else -num
    
    return answer